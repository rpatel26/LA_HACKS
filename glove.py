from pygame import *
#import sys
import time
#sys.exit()

volume_input = 0.5
song1 = 'seagulls.ogg'
effect1 = 'sample_ogg.ogg'
effect2 = 'john_cena.ogg'

time_in = 0
Break_option = 0
currentSong = 0 
mixer.init()  # Initialize mixer
playing = 1
isPause = False
isEffect = False
stopEffect = False
stopSong = False
channel_no = 1
song_array = (song1) 
effect_array = (effect1, effect2)

#Pause toggle function
def toggle_pause(channel_Number):
	if playing==1:
		mixer.Channel(channel_Number).pause()
		playing = 0
	else :
		mixer.Channel(channel_Number).unpause()
		playing = 1

#Volume control function - analog data 
def changeVolume(channel_Number, vol):
	mixer.Channel(channel_Number).set_volume(vol)
	volume_input = vol

#fade out function - boolean and analog fade/no fade
def fadeOut(channel_Number, time1):
	mixer.Channel(channel_Number).fadeout(time1)

#add effect function
def new_effect(channel_Number, fileName):
	mixer.Channel(channel_Number).play(mixer.Sound(fileName))
	mixer.Channel(channel_Number).set_volume(int(volume_input/2))

#complete stop of song playing funciton
def stop(channel_Number):
	mixer.Channel(channel_Number).stop()

mixer.Channel(currentSong).play(mixer.Sound(song1))      # Play the music file


while mixer.Channel(currentSong).get_busy():
	# Pause toggle
	if isPause == True:
		toggle_pause(currentSong)
   
	changeVolume(currentSong, volume_input)    
  
	if time_in>= 2000: 
		fadeOut(currentSong,time_in)    #amount by which you bend the flex sensor --> inversely proportonal to the time it takes to fade
		
	i = 0
	if isEffect == True: 
		new_effect(channel_no,effect(i))
		i+=1
		if i == 2:
			i = 0
		
	if stopEffect == True:
		stop(channel_no)
	
	if stopSong == True:
		stop(currentSong)
		stop(channel_no)


