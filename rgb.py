# Python program to use an RGB LED
# Hardware: 1xRGB LED, 3x 220 hom resistor
# Wiring: GND to catode, pin 11 to Red, pin 13 to Green, pin 15 to Blue


## Libraries to import##
import RPi.GPIO as GPIO
from time import sleep


## General Setup ##
GPIO.setmode(GPIO.BOARD) # Use the board pin numbering system
GPIO.setwarnings(False)  # Disable warning at runtime 
#redPin = 11
#greenPin = 13
#bluePin = 15

RGB = [11,13,15]         # Set a list for the RGB GPIO Pin


## Sets pin each pins to output and to LOW
for pin in RGB:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)



## Simple check on the RGB value passed in
def validColor(aColor):
	#print(aColor)
	result = True
	for bit in aColor:
		#print(bit)
		if (bit != "0" and  bit != "1"):
			return  False

	return result



try:
	while(True):
		request = input("Select your color: ")
		if (len(request)== 3 and validColor(request) ):
			index = 0
			for pin in RGB:
				GPIO.output(pin,int(request[index]))
				index = index + 1

		else:
			print("Wrong input...")

except KeyboardInterrupt:
	GPIO.cleanup()
	exit
finally:
	print("Goodbye! \n")



