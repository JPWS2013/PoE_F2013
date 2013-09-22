import math #Imports math to do trig calculations

class lidar: #Definition of a new class called lidar
	def __init__(self, input_horz_ang=0, input_vert_ang=0, radius=0):
		horz_ang=math.radians(input_horz_ang) #converts the horizontal angle from degrees to radians
		vert_ang=math.radians(input_vert_ang) #converts the vertical angle from degrees to radians
		
		self.z_pos = -radius*math.cos(vert_ang) #Calculates the length of the position vector projected on the z-axis
		self.y_pos = radius*math.sin(vert_ang)*math.sin(horz_ang) #Calculates the length of the position vector projected onto the y axis
		self.x_pos = radius*math.sin(vert_ang)*math.cos(horz_ang) #Calculates the length of the position vector projected onto the x axis

	def display_data(self): #Instance method to display the data encapsulated in the lidar object

	 	print "X Position = ", self.x_pos
		print "Y Position = ", self.y_pos
		print "Z Position = ", self.z_pos