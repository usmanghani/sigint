import sys
from os import path
import numpy as np

from IPython import embed
from math import ceil
from pydub import AudioSegment

import speech_recognition as sr
r = sr.Recognizer()

from config import IBM_USERNAME
from config import IBM_PASSWORD
from config import WIT_AI_KEY
from config import HOUNDIFY_CLIENT_ID
from config import HOUNDIFY_CLIENT_KEY
from config import BING_KEY
from config import API_AI_CLIENT_ACCESS_TOKEN


def transcribe_audio_file(audio_file):
    with sr.AudioFile(audio_file) as source:
        segments = segment_audio(source)

    return "\n".join(recognize_google(seg) for seg in segments)


def segment_audio(source):
    # simple 10 second chunks
    return [r.record(source, duration=10) for _ in range(int(ceil(source.DURATION/10.)))]

    # from pyAudioAnalysis import audioBasicIO as aIO
    # from pyAudioAnalysis import audioSegmentation as aS
    # # [Fs, x] = aIO.readAudioFile(audio_file)
    # [Fs, x] = aIO.readAudioFile('temp.wav')
    # segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, Weight = 0.3, plot = False)


def recognize_google(audio):
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Google Speech Recognition service; {0}".format(e)


def recognize_ibm(audio):
    # recognize speech using IBM Speech to Text
    try:
        return r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    except sr.UnknownValueError:
        print "IBM Speech to Text could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from IBM Speech to Text service; {0}".format(e)
    return None

def recognize_wit(audio):
    # recognize speech using Wit.ai
    try:
        return r.recognize_wit(audio, key=WIT_AI_KEY)
    except sr.UnknownValueError:
        print "Wit.ai could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Wit.ai service; {0}".format(e)

# doesn't exist ??? idk wtf lol
def recognize_houndify(audio):
    # recognize speech using Houndify
    try:
        return r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
    except sr.UnknownValueError:
        print "Houndify could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Houndify service; {0}".format(e)

# doesn't work on osx
def recognize_sphinx(audio):
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Google Speech Recognition service; {0}".format(e)

# broken
def recognize_bing(audio):
    # recognize speech using Microsoft Bing Voice Recognition
    try:
        return r.recognize_bing(audio, key=BING_KEY)
    except sr.UnknownValueError:
        print "Microsoft Bing Voice Recognition could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e)

# broken
def recognize_api(audio):
    # recognize speech using api.ai
    try:
        return r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)
    except sr.UnknownValueError:
        print "api.ai could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from api.ai service; {0}".format(e)



audio_file = sys.argv[-1]
audio_file = path.join(path.dirname(path.realpath(__file__)), audio_file)
#
# audio = AudioSegment.from_mp3(audio_file)
#
# AUDIO_FILE = 'abcd.wav'
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source) # read the entire audio file

print transcribe_audio_file(audio_file)
# embed()

# seg1 = segment[241*1000:250*1000]
# # from pydub.playback import play
# # play(seg1)
# seg1.export(out_f='temp.wav', format='wav', codec='flac')
