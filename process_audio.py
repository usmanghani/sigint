from pydub import AudioSegment
from pydub.silence import split_on_silence

import os

mp3_files = filter(lambda x: x.endswith('mp3'), os.listdir('.'))

segment = AudioSegment.from_mp3(mp3_files[0])
segments_split_on_silence = split_on_silence(segment)



