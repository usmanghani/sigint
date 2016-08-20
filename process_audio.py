from pydub import AudioSegment

from glob import glob

mp3_files = filter(lambda x: x.endswith('mp3'), glob('*.mp3'))

segment = AudioSegment.from_mp3(mp3_files[0])

# from pydub.silence import split_on_silence
# segments_split_on_silence = split_on_silence(segment)

seg1 = segment[45*1000:75*1000]
from pydub.playback import play
play(seg1)
from pydub.utils import mediainfo
mediainfo(mp3_files[0])
with seg1.export(out_f='abcd.wav', format='wav', codec='flac') as exported_file:
    pass

mediainfo('abcd.wav')

# from google_speech_api_test import do_stream
# recognize(seg1.raw_data)








