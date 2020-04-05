import RPi.GPIO as GPIO
import time
import socket
import sys
import fcntl
import struct
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

hostname = socket.gethostname()

def get_ip_address():
	ip_address = '';
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))
	ip_address = s.getsockname()[0]
	s.close()
	return ip_address

blinks = 4
try:
	while (blinks < 5):
		GPIO.output(7, 1)
		GPIO.output(11, 1)
		time.sleep(1)
		GPIO.output(7,0)
		GPIO.output(11,0)
		time.sleep(1)
		blinks = blinks + 1
#		print("Blinked")

except KeyboardInterrupt:
	GPIO.cleanup()
	exit
GPIO.cleanup()

print(get_ip_address())
