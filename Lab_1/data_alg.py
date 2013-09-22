import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import serial
import time
from lidar_classdef import *

ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use 

data=[] #List object that stores the data from the arduino
counter=0 #Counter that counts how many data points it has taken (May not be needed for final code)

horizontal_angle_track=130
vertical_angle_track=0

print "Waiting for arduino to be ready....."

time.sleep(1)

print "Programme beginning now"

time.sleep(1)

#Moves the servo to the starting position

ser.write('5')
horizontal_angle_track=130
time.sleep(0.5)
ser.write('6')
vertical_angle_track=90

horz_angle=range(horizontal_angle_track, 45, -1)
vert_angle=range(vertical_angle_track,vertical_angle_track+1,1)

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

		distance_response=ser.readline()
		cleanReading=distance_response[0:-2] #Removes the last 2 characters ("\r\n") from the arduino output
		distance=float(cleanReading) #Type-casts it as an integer so that it can be plotted
		print "distance= ", distance

		ser.write('8')

		angle_response=ser.readline()

		cleanReading=angle_response[0:-2] #Removes the last 2 characters ("\r\n") from the arduino output
		seperator_index=cleanReading.index(',')
		vertical_angle=cleanReading[0:seperator_index]
		vertical_angle=int(vertical_angle)
		print "vertical_angle= ", vertical_angle
		horizontal_angle=cleanReading[(seperator_index+1): ]
		horizontal_angle=int(horizontal_angle)
		print "horizontal_angle= ", horizontal_angle

		processed_full_data_holder=lidar(horizontal_angle, vertical_angle, distance)

		data.append(processed_full_data_holder)

		ser.write('1')
		horizontal_angle_track=horizontal_angle_track-2
		#print 'horizontal_angle_track= ', horizontal_angle_track
		#time.sleep(0.5)

	ser.write('3')
	vertical_angle_track=vertical_angle_track+3
	#print 'direction_track= ', direction_track
	time.sleep(0.5)

	ser.write('5')
	horizontal_angle_track=140
	time.sleep(0.5)

for eachData in data:
	eachData.display_data()


#def randrange(n, vmin, vmax):
#    return (vmax-vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# '''n = 100
# for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zl, zh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)'''

xs = []
ys = []
zs = []

for eachPoint in data:
	xs.append(eachPoint.x_pos)
	ys.append(eachPoint.y_pos)
	zs.append(eachPoint.z_pos)

ax.scatter(xs,ys,zs, c ='r', marker = 'o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()