"""Google Cloud Speech API sample application using the REST API for batch
processing."""

import argparse
import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


def get_storage_service():
    credentials = GoogleCredentials.from_stream('API Project-d5ad24801c2f.json').create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'storage', 'v1', http=http, discoveryServiceUrl=DISCOVERY_URL)


def get_speech_service():
    # credentials = GoogleCredentials.get_application_default().create_scoped(
    #     ['https://www.googleapis.com/auth/cloud-platform'])
    credentials = GoogleCredentials.from_stream('API Project-d5ad24801c2f.json').create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)


def store_object(file_path):
    import os
    service = get_storage_service()
    service_request = service.objects().insert(bucket='audio_test', body={
        'name': os.path.basename(file_path),
    }, media_body=file_path)
    response = service_request.execute()
    print(json.dumps(response))


def recognize(input_speech):
    speech_content = base64.b64encode(input_speech)

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                'encoding': 'FLAC',  # raw 16-bit signed LE samples
                #'sampleRate': 16000,  # 16 khz
                'sampleRate': 44100,  # 44 khz
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                # 'uri':
                }
            })
    response = service_request.execute()
    print(json.dumps(response))


def main(speech_file):
    """Transcribe the given audio file.

    Args:
        speech_file: the name of the audio file.
    """
    with open(speech_file, 'rb') as speech:
        recognize(speech.read())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
    main(args.speech_file)