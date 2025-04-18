#!/usr/local/bin/python
import sys
import mido

mid = mido.MidiFile(sys.argv[1])

for msg in mid:
    print(msg)
#for i, track in enumerate(mid.tracks):
#    print('Track {}: {}'.format(i, track.name))
#    for msg in track:
#        print(msg)
#for msg in mid.play():
#    print(msg)
