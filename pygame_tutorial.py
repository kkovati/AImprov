import pygame
import time
import io

# audibilize

def play_file(path):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)

    pygame.mixer.music.load(path)

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def play_midi_obj(midi_file):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)

    midi_buffer = io.BytesIO()
    midi_file.save(file=midi_buffer)
    midi_buffer.seek(0)
    pygame.mixer.music.load(midi_buffer)

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def main():
    midi_file = 'example.mid'
    play_file(midi_file)


if __name__ == '__main__':
    main()
