
from pygame import *
import sys
#sys.exit()
file = 'sample_ogg.ogg'
command = 0
mixer.init()  # Initialize mixer
mixer.music.load(file)  # Load the music file
Playing = 1
mixer.music.play()      # Play the music file


while mixer.music.get_busy():
    glove_input = int(input("Pause or Play?"))
    command = glove_input
    if command:
        if Playing:
            mixer.music.pause()
            Playing = 0
        else:
            mixer.music.unpause()
            Playing = 1