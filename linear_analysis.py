import sys
import numpy as np
from pydub import AudioSegment

def transcribe_audio_file(filename):
    import speech_recognition as sr
    from os import path
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file

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




audio_file = sys.argv[-1]

segment = AudioSegment.from_mp3(audio_file)


# seg1 = segment[241*1000:250*1000]
# # from pydub.playback import play
# # play(seg1)
# seg1.export(out_f='temp.wav', format='wav', codec='flac')



# print transcribe_audio_file('temp.wav')


from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
# [Fs, x] = aIO.readAudioFile(audio_file)
[Fs, x] = aIO.readAudioFile('temp.wav')
segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, Weight = 0.3, plot = False)
