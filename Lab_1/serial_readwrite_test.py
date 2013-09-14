#This code is somewhat pseudocode intended to simulate the programme that would control the entire process of taking a sweep of the surroundings to produce a map using the IR sensor

import serial
import time

ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use 

data=[] #List object that stores the data from the arduino
counter=0 #Counter that counts how many data points it has taken (May not be needed for final code)

angle=range(1,3,1)

time.sleep(3)

for eachVerticalAngle in angle:
	print "Vertical Angle = ", eachVerticalAngle
	print "I'm sending code to the arduino to reset it back all the way to the left"
	time.sleep(1)
	ser.write('5')

	response=ser.readline()

	print response

	for eachHorizontalAngle in angle:
		print "I'm sending the code to the arduino to turn the servo 1 degree to the right"
		print "Degree = ", eachHorizontalAngle
		time.sleep(1)
		ser.write('1')

		response=ser.readline()

		print response

		time.sleep(1)

		print "I'm asking the arduino to take a reading now"
		time.sleep(1)
		ser.write('6')

		response=ser.readline()

		print "Reading = ", response