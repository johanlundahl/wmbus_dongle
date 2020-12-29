import serial

print('Serial communication')
ser = serial.Serial('/dev/ttyS0', 9600)
at = 'AT'.encode()
print('Writing', at)
#ser.write(at)
ser.write(b'0x41 0x54')

print('Reading...')
received_data = ser.read()
print(received_data)
