
from pygame import *
#import sys
#sys.exit()
file = 'Swedish_1_ogg.ogg'
command = 0
volume_input = 0.5
effect_1 = 'happy_ogg.ogg'

Break_option = 0

mixer.init()  # Initialize mixer
#mixer.Channel(0).load(file)  # Load the music file
Playing = 1
mixer.Channel(0).play(mixer.Sound(file))      # Play the music file


while mixer.Channel(0).get_busy():
    # Pause and Play Effects
    glove_input = int(input("Pause or Play?"))
    command = glove_input
    if command:
        if Playing:
            mixer.Channel(0).pause()
            Playing = 0
        else:
            mixer.Channel(0).unpause()
            Playing = 1

    # Volume Up and Down Effects
    volume_input = float(input("Input Volume Level"))
    mixer.Channel(0).set_volume(volume_input)

    # Fade Out Effect
    fade_input = int(input("Fade out?"))  # Give 1 for fade out, 0 otherwise
    if fade_input:
        mixer.Channel(0).fadeout(5000)

    # Drum Effects
    drum_input = int(input("Add second song?"))
    if drum_input:
        mixer.Channel(1).play(mixer.Sound(effect_1))
        mixer.Channel(1).set_volume(volume_input)

    else:
        mixer.Channel(1).play(mixer.Sound(effect_1))
        mixer.Channel(1).set_volume(0)

    #Functionality To Stop
    Break_option = int(input("Break Option?"))
    if Break_option == 1:
        break
    else:
        continue