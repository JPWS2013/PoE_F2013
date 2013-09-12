import serial

ser=serial.Serial('/dev/tty', 9600)

while True:
print ser.readline()