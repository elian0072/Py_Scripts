# Purpose of your script
# Requierements
# Author
# Date



## Libraries ## 
import RPi.GPIO as GPIO
from time import sleep

## Raspberry Pi setup ##
GPIO.setmode(GPIO.BOARD) # Use the board pin numbering system
GPIO.setwarnings(False)  # Disable warning at runtime

## Variables ##
pin = 15


## Pin Initialization ##
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, 0)


## Functions ##
def main():
	print("Code for your main function")



## MAIN ##
try:
	## Code goes here ##
	main()

except KeyboardInterrupt:
	GPIO.cleanup()
	exit
finally:
	print("Exiting... \n")
