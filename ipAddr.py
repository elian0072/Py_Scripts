# Python script to display the Raspberry Pi IP address


## Libraries ##
import socket

## Variabales ##
hostname = socket.gethostname()


## Function to get the IP address ##
def get_ip_address():
	ip_address = '';
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))
	ip_address = s.getsockname()[0]
	s.close()
	return ip_address

## MAIN ##
def main():

	print(get_ip_address())


main()
