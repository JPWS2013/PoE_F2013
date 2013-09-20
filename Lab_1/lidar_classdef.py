import math
class lidar:
	def __init__(self, input_horz_ang=0, input_vert_ang=0, radius=0):
		horz_ang=math.radians(input_horz_ang)
		vert_ang=math.radians(input_vert_ang)
		r=radius
		
		self.z_pos = r*math.sin(vert_ang)
		self.y_pos = r*math.cos(vert_ang)*math.sin(horz_ang)
		self.x_pos = r*math.cos(vert_ang)*math.cos(horz_ang)

	def display_data(self):

	 	print "X Position = ", self.x_pos
		print "Y Position = ", self.y_pos
		print "Z Position = ", self.z_pos