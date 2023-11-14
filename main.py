from mido import Message, MidiFile, MidiTrack
import rtmidi
from numpy.random import choice

import pygame_tutorial


class Scale:
    pass


class BluesScale(Scale):
    base_notes = [60, 63, 65, 66, 67, 70]


def make_random_track(scale):
    note_range = []
    for note in scale.base_notes:
        note_range.append(note - 12)
    note_range.extend(scale.base_notes)
    for note in scale.base_notes:
        note_range.append(note + 12)
    assert len(note_range) == 18

    prev_note_idx = 12
    note_list = [note_range[prev_note_idx]]
    for i in range(99):
        if prev_note_idx <= 2:
            note_candidates = [0, 1, 2, 3, 4]
        elif prev_note_idx >= 15:
            note_candidates = [13, 14, 15, 16, 17]
        else:
            note_candidates = [prev_note_idx - 2, prev_note_idx - 1, prev_note_idx,
                               prev_note_idx + 1, prev_note_idx + 2]
        curr_note_idx = choice(note_candidates, size=1, p=(.2, .25, .1, .25, .2))[0]
        note_list.append(note_range[curr_note_idx])

    return note_list


def main():
    track = MidiTrack()
    mid = MidiFile(type=0)  # type 0 (single track): all messages are saved in one track
    mid.tracks.append(track)
    # mid.add_track(track)
    # mid.save('example.mid')

    notes = make_random_track(BluesScale)

    track.append(Message('program_change', program=1, time=0))
    for note in notes:
        note_time = choice([125, 250], size=1, p=(.7, .3))[0]
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=note_time))

    pygame_tutorial.play_midi_obj(midi_file=mid)


if __name__ == '__main__':
    main()
