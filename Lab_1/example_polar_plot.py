import numpy as np
import matplotlib.pyplot as plt
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





r = np.arange(0, 3.0, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, polar=True)
ax.plot(theta, r, color='r', linewidth=3)
ax.set_rmax(2.0)
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()