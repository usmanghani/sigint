import sys
import numpy as np

from IPython import embed
from math import ceil
from pydub import AudioSegment


import speech_recognition as sr

def transcribe_audio_file(filename):
    from os import path
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        segments = [r.record(source, duration=10) for _ in range(int(ceil(source.DURATION/10.)))]

    embed()

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


def segment_audio(audio, dumb=True):

    if dumb:
        pass

    # from pyAudioAnalysis import audioBasicIO as aIO
    # from pyAudioAnalysis import audioSegmentation as aS
    # # [Fs, x] = aIO.readAudioFile(audio_file)
    # [Fs, x] = aIO.readAudioFile('temp.wav')
    # segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, Weight = 0.3, plot = False)

audio_file = sys.argv[-1]
#
# audio = AudioSegment.from_mp3(audio_file)
#
# AUDIO_FILE = 'abcd.wav'
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source) # read the entire audio file

transcribe_audio_file(audio_file)
# embed()

# seg1 = segment[241*1000:250*1000]
# # from pydub.playback import play
# # play(seg1)
# seg1.export(out_f='temp.wav', format='wav', codec='flac')
