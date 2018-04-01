from pygame import *
#import sys
import time
#sys.exit()

volume_input = 0.5

def pause(song):
	mixer.Channel(song).pause()

def play(song):
	mixer.Channel(song).unpause()

def changeVolume(song, value):
	mixer.Channel(song).set_volume(value)
        volume_value = value


def fadeOut(song, value):
	mixer.Channel(song).fadeout(value)

def drumEffect(song, preVolume, fileName):
	mixer.Channel(song).play(mixer.Sound(fileName))
        mixer.Channel(song).set_volume(int(preVolume/2))

def stop(song):
	mixer.Channel(song).set_volume(0)


file1 = 'Swedish_1_ogg.ogg'
#command = 0
effect_1 = 'happy_ogg.ogg'

Break_option = 0
currentSong = 0
mixer.init()  # Initialize mixer
#mixer.Channel(0).load(file)  # Load the music file
Playing = 1
mixer.Channel(currentSong).play(mixer.Sound(file1))      # Play the music file



while mixer.Channel(0).get_busy():
    # Pause and Play Effects
    if pause == True:
        pause(currentSong)
        time.sleep(3)
        pause = False
    else:
        play(currentSong)
        time.sleep(3)
        pause = True
   

    changeVolume(currentSong, int(volume_input/2))    
   
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



