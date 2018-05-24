#!/usr/bin/env python2.7

from subprocess import call
from num2words import num2words
from random import randint

import pygame
import time
import random
import RPi.GPIO as GPIO

cmd_beg = 'espeak '
cmd_end = ' 2>/dev/null'
introTxt = "Hello cunt I am ready to recieve your punch" #startup sound
introTxt = introTxt.replace(' ', '_')
shock_pin = 17 
ldpht = "/home/pi/Desktop/shock_alarm/"
cursong = 0

sounds = ["chickencoop.mp3","where is my team.mp3","whaaat.mp3","goingtobed.mp3"]
soundslen = len(sounds)


GPIO.setmode(GPIO.BCM)
GPIO.setup(shock_pin, GPIO.IN)

call([cmd_beg+introTxt+cmd_end], shell=True)
pygame.mixer.init()
def callback(shock_pin):
        if GPIO.input(shock_pin):
            if pygame.mixer.music.get_busy() == False:
                print ("alarm time")
                #pygame.mixer.init()
                cursong = randint(0,soundslen-1)
                pygame.mixer.music.load(ldpht+sounds[cursong])#35
                pygame.mixer.music.play()

        else:
            print ("alarm time2")


GPIO.add_event_detect(shock_pin, GPIO.BOTH, bouncetime=500)
GPIO.add_event_callback(shock_pin, callback)

while True:
    time.sleep(500)
