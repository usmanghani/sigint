import sys
from pydub import AudioSegment


mp3_file = sys.argv[-1]

segment = AudioSegment.from_mp3(mp3_file)

# from pydub.silence import split_on_silence
# segments_split_on_silence = split_on_silence(segment)

seg1 = segment#[510*1000:525*1000]
# from pydub.playback import play
# play(seg1)
from pydub.utils import mediainfo
print mediainfo(mp3_file)
with seg1.export(out_f='abcd.wav', format='wav', codec='flac') as exported_file:
    pass
print "----"
print "----"
print mediainfo('abcd.wav')



import speech_recognition as sr
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "abcd.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print "Google Speech Recognition thinks you said ", r.recognize_google(audio)
except sr.UnknownValueError:
    print "Google Speech Recognition could not understand audio"
except sr.RequestError as e:
    print "Could not request results from Google Speech Recognition service; {0}".format(e)
