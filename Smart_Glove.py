
from pygame import *
import sys
#sys.exit()
file = 'sample_ogg.ogg'
command = 0
volume_input = 0.5

mixer.init()  # Initialize mixer
mixer.music.load(file)  # Load the music file
Playing = 1
mixer.music.play()      # Play the music file


while mixer.music.get_busy():
    # Pause and Play Effects
    glove_input = int(input("Pause or Play?"))
    command = glove_input
    if command:
        if Playing:
            mixer.music.pause()
            Playing = 0
        else:
            mixer.music.unpause()
            Playing = 1

    # Volume Up and Down Effects
    volume_input = float(input("Input Volume Level"))
    mixer.music.set_volume(volume_input)

    # Fade Out Effect
    fade_input = int(input("Fade out?"))  # Give 1 for fade out, 0 otherwise
    if fade_input:
        mixer.music.fadeout(5000)

    #





