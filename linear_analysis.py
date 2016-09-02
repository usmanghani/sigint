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

    segments = segments[:12]


    audio = {
        "google": [recognize_google(seg) for seg in segments],
        "ibm": [recognize_ibm(seg) for seg in segments],
        "wit": [recognize_wit(seg) for seg in segments]
    }

    return audio


def segment_audio(source):
    # simple 10 second chunks
    return [r.record(source, duration=10) for _ in range(int(ceil(source.DURATION/10.)))]

    # from pyAudioAnalysis import audioBasicIO as aIO
    # from pyAudioAnalysis import audioSegmentation as aS
    # # [Fs, x] = aIO.readAudioFile(audio_file)
    # [Fs, x] = aIO.readAudioFile('temp.wav')
    # segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, Weight = 0.3, plot = False)


def recognize_google(audio):
    print "g"
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
    print "i"
    # recognize speech using IBM Speech to Text
    try:
        return r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    except sr.UnknownValueError:
        print "IBM Speech to Text could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from IBM Speech to Text service; {0}".format(e)
    return None

def recognize_wit(audio):
    print "w"
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

audio = transcribe_audio_file(audio_file)

f = open('audio_out', 'w')
f.write(repr(audio))
f.close()
# embed()

# seg1 = segment[241*1000:250*1000]
# # from pydub.playback import play
# # play(seg1)
# seg1.export(out_f='temp.wav', format='wav', codec='flac')


def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

wit = [ i.strip() for i in audio['wit']]
google = [ i.strip() for i in audio['google']]
ibm = [ i.strip() for i in audio['ibm']]
ibm2 = [i.replace('\n','') for i in ibm]

gw = [levenshteinDistance(g,w) for g,w in zip(google, wit)]
gi = [levenshteinDistance(g,i) for g,i in zip(google, ibm)]
gi2 = [levenshteinDistance(g,i) for g,i in zip(google, ibm2)]
iw = [levenshteinDistance(w,i) for w,i in zip(ibm, wit)]
i2w = [levenshteinDistance(w,i) for w,i in zip(ibm2, wit)]

gdist = sum(gw)+sum(gi)
wdist = sum(gw)+sum(iw)
idist = sum(gi)+sum(iw)
i2dist = sum(gi2)+sum(i2w)
print "google", gdist
print "ibm1", idist
print "ibm clean", i2dist
print "wit", wdist
