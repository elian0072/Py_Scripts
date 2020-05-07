# Control an output from a button
# a button
# Jaime Balbuena
# 07/05/2020



## Libraries ## 
import RPi.GPIO as GPIO
from time import sleep

## Raspberry Pi setup ##
GPIO.setmode(GPIO.BOARD) # Use the board pin numbering system
GPIO.setwarnings(False)  # Disable warning at runtime

## Variables ##
LED = 3
btn = 5
ledState = False
pressed = False
btnState = True
previous = True

## Pin Initialization ##
GPIO.setup(LED, GPIO.OUT, initial = 0)
GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



## Functions ##
def main():
	print("Code for your main function")



## MAIN ##
try:
	## Code goes here ##
	main()
	while True:
		GPIO.output(LED, GPIO.input(btn))
		#btnState = GPIO.input(btn)
		#if (previous != btnState and btnState == pressed):
		#	ledState = not ledState
		#	GPIO.output(LED, ledState)
		#previous = btnState
		#sleep(.01)
		
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Keyboard interrupt. Bye Bye")
	exit
finally:
	print("Exiting... \n")
