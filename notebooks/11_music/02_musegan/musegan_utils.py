import music21
from music21 import midi
import numpy as np
from matplotlib import pyplot as plt


def binarise_output(output):
    # output is a set of scores: [batch size , steps , pitches , tracks]
    max_pitches = np.argmax(output, axis=3)
    return max_pitches


def notes_to_midi(output, n_bars, n_tracks, n_steps_per_bar, filename):
    for score_num in range(len(output)):
        max_pitches = binarise_output(output)
        midi_note_score = max_pitches[score_num].reshape(
            [n_bars * n_steps_per_bar, n_tracks]
        )
        parts = music21.stream.Score()
        parts.append(music21.tempo.MetronomeMark(number=66))
        for i in range(n_tracks):
            last_x = int(midi_note_score[:, i][0])
            s = music21.stream.Part()
            dur = 0
            for idx, x in enumerate(midi_note_score[:, i]):
                x = int(x)
                if (x != last_x or idx % 4 == 0) and idx > 0:
                    n = music21.note.Note(last_x)
                    n.duration = music21.duration.Duration(dur)
                    s.append(n)
                    dur = 0
                last_x = x
                dur = dur + 0.25
            n = music21.note.Note(last_x)
            n.duration = music21.duration.Duration(dur)
            s.append(n)
            parts.append(s)
        parts.write(
            "midi", fp="./output/{}_{}.midi".format(filename, score_num)
        )


def draw_bar(data, score_num, bar, part):
    plt.imshow(
        data[score_num, bar, :, :, part].transpose([1, 0]),
        origin="lower",
        cmap="Greys",
        vmin=-1,
        vmax=1,
    )


def draw_score(filename, score_num):
    mf = midi.MidiFile()
    mf.open("./output/{}_{}.midi".format(filename, score_num))
    mf.read()
    mf.close()
    return midi.translate.midiFileToStream(mf)
