import time
import socket
import struct
from random import random

#Function to generate random data to send
def gen_data_msg(num_signals):
	data = bytearray()
	for i in range(num_signals):
		#Generate random number between 0 and 100 and package as f32 (single).
		sig = 100*random()
		data.extend(bytearray(struct.pack("f", sig)))
		print("Sig" + str(i) + " = " + str(sig))
	
	#Add header to package with total package size. Header is U16.
	size_header = bytearray(struct.pack("H", len(data) + 2))
	msg = size_header + data
	return msg

#Send data to localhost in port 61557 server
serv_IP = "127.0.0.1"
serv_PORT = 61557
server_add = (serv_IP, serv_PORT)

#Create UDP socket to send data to server
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while(1):
	#Run continously until interrupted by the keyboard
	try:
		#Build message to send and print it on console. Message will contain 4 numbers
		MESSAGE = gen_data_msg(4)
		print(MESSAGE)
		#Send through UDP socket
		sock.sendto(MESSAGE, server_add)
		#Wait 2 seconds before the next iteration
		time.sleep(2)
	except KeyboardInterrupt:
		break

#Close UDP socket and finish program after keyboard interruption		
print("Closing UDP socket")
sock.close()

