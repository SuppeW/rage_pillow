#!/usr/bin/env python3

from num2words import num2words
from subprocess import call

cmd_beg= 'espeak'
cmd_end= ' | aplay home/pi/Desktop/text.mav 2>/dev/null'
cmd_out= '--stdout> /home/pi/Desktop/Text.mav'

text = input("Enter text here: ")
print(text)

text = text.replace(' ', '_')

call([cmd_beg+cmd_out+text+cmd_end], shell=True)