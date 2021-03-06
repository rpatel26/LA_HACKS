import mraa
import time


gpio_array = [mraa.Gpio(23), mraa.Gpio(24), mraa.Gpio(25), mraa.Gpio(26), mraa.Gpio(27), mraa.Gpio(29), mraa.Gpio(30), mraa.Gpio(31),mraa.Gpio(32), mraa.Gpio(33)] 

test = mraa.Gpio(34)
test.dir(mraa.DIR_OUT)

while True:
    print(test.write(1))


for i in gpio_array:
	i.dir(mraa.DIR_IN)

def read_data():
	data = []
	for i in gpio_array:
		data.append(i.read())
	my_integer = "".join(map(str,data))
	return int(my_integer) 

from pygame import *

volume_input = 0.5
song1 = 'seagulls.ogg'
effect1 = 'sample_ogg.ogg'
effect2 = 'Clickz.ogg'
effect3 = 'Badum-tss.ogg'
effect4 = 'BeatDrop.ogg'
effect5 = 'Echoes.ogg'

number = 0
ef_1 = False
ef_2 = False
ef_3 = False
ef_4 = False
ef_5 = False
vol_on = False
vol_off = False
fade_on = False
stop_ef = False

time_in = 0
currentSong = 0 
mixer.init()  # Initialize mixer
isPause = False
isPlay = False
isEffect = False
stopEffect = False
stopSong = False
channel_no = 1
song_array = (song1) 
effect_array = (effect1, effect2, effect3, effect4, effect5)

#Pause function
def pause(channel_Number):
		mixer.Channel(channel_Number).pause()

#Play function	
def play(channel_Number):
		mixer.Channel(channel_Number).unpause()
		

#Volume control function - analog data 
def changeVolume(channel_Number, vol):
	mixer.Channel(channel_Number).set_volume(vol)
	volume_input = vol

#fade out function -  boolean and analog fade/no fade
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


def digital(data):
	if data == 0:
		stop_ef = True
	elif data == 1:
		isPause = True
	elif data == 10:
		isPlay = True
	elif data == 11:
		vol_on = True
	elif data == 100:
		Vol_off = True
	elif data == 101:
		fade_on = True
	elif data == 110:
		stopSong = True
	elif data == 111:
		ef_1 = True
	elif data == 1000:
		ef_2 = True
	elif data == 1001:
		ef_3 = True
	elif data == 1010:
		ef_4 = True
	elif data == 1011:
		ef_5 = True
	elif data == 1101:
		isEffect = True
	else:
		number = int(str(data),2)
		
		


while mixer.Channel(currentSong).get_busy():
	#calling the digital function	
	digital(read_data())
	if number <518 & number>12 :
		volume_input = number/506
	else:
		time_in = 3000 + (number/506)*4000

	# Pause function
	if isPause == True:
		pause(currentSong)
                isPause = False
                print "pause"

	if isPlay == True:
		play(currentSong)
                isPlay = False
                print "play"
   
	if vol_on == True:
		changeVolume(currentSong, volume_input)
                print "changing volume"

	if vol_off == True:
		vol_on = False		
		
	if fade_on == True:
		fadeOut(curentSong,time_in)    #amount by which you bend the flex sensor --> inversely proportonal to the time it takes to fade
                print "fading"

	if stopSong == True:
		stop(currentSong)
		stop(channel_no)				
                print "stop song"

	if isEffect == True: 
		if ef_1 == True:
			new_effect(channel_no,effect[0])
		elif ef_2 == True:
			new_effect(channel_no, effect[1])
		elif ef_3 == True:
			new_effect(channel_no, effect[2])
		elif ef_4 == True:
			new_effect(channel_no, effect[3])
		elif ef_5 == True:
			new_effecct(channel_no, effect[4])
		
		
	if stop_ef == True:
		stop(channel_no)    
	
