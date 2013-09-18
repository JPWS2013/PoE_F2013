import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import serial
import time
from lidar_classdef import *

ser=serial.Serial('/dev/ttyACM1', 9600) #Defines the serial port to use 

data=[] #List object that stores the data from the arduino
counter=0 #Counter that counts how many data points it has taken (May not be needed for final code)

horz_angle=range(1,90,5)
vert_angle=range(1,45,3)

horizontal_angle_track=0
vertical_angle_track=0

print "Waiting for arduino to be ready....."

time.sleep(5)

print "Programme beginning now"

time.sleep(1)

#Moves the servo to the starting position

ser.write('5')
time.sleep(0.5)
ser.write('6')

direction_track=1

for eachVerticalAngle in vert_angle:	
	#print "I'm sending code to the arduino to reset it back all the way to the left"
	#time.sleep(1)
	#ser.write('1')

	#response=ser.readline()

	#print response

	for eachHorizontalAngle in horz_angle:
		#print "I'm sending the code to the arduino to turn the servo 1 degree to the right"
		#print "Degree = ", eachHorizontalAngle
		#time.sleep(1)
		ser.write('7')

		response=ser.readline()
		cleanReading=response[0:-2] #Removes the last 2 characters ("\r\n") from the arduino output
		cleanReading=int(cleanReading) #Type-casts it as an integer so that it can be plotted
		distance=25732.834527*cleanReading**(-1.1314581);

		processed_full_data_holder=lidar(horizontal_angle_track, vertical_angle_track, distance)

		data.append(processed_full_data_holder)

		ser.write('1')
		horizontal_angle_track=horizontal_angle_track+5
		#print 'horizontal_angle_track= ', horizontal_angle_track
		time.sleep(0.5)

	ser.write('3')
	vertical_angle_track=vertical_angle_track+3
	#print 'direction_track= ', direction_track
	time.sleep(0.5)

	ser.write('5')
	horizontal_angle_track=0
	time.sleep(0.5)

for eachData in data:
	eachData.display_data()
# def randrange(n, vmin, vmax):
#     return (vmax-vmin)*np.random.rand(n) + vmin

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# '''n = 100
# for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zl, zh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)'''

# xs = [1,2,3]
# ys = [1,2,3]
# zs = [1,2,3]

# ax.scatter(xs,ys,zs, c ='r', marker = 'o')

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()