import serial

ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use 

data=[] #List object that stores the data from the arduino
counter=0 #Counter that counts how many data points it has taken (May not be needed for final code)

while True: #While able to get data?
	while counter!=30: #Until it has 30 data points
		reading= ser.readline() #Read the output from the arduino through the serial port

		if counter != 0: #Ignores the very first reading from the arduino becuase that is usually a junk reading
			cleanReading=reading[0:-2] #Removes the last 2 characters ("\r\n") from the arduino output
			cleanReading=int(cleanReading) #Type-casts it as an integer so that it can be plotted
			data.append(cleanReading) #Appends it to the data list
		
		counter += 1 #Increments the counter

		print counter #This is here just so that there is an output to tell the user how many data points have been stored

	break #Once it's done getting the data, break the while loop

print data #Display the data on screen