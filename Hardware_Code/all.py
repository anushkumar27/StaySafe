import RPi.GPIO as GPIO
import serial
from time import sleep
import sys
import thread

testCase = int(sys.argv[1])
ser = serial.Serial('/dev/ttyACM0', 9600)

# blinking function
def blink(pin):
	if(pin == 7):
		GPIO.output(11,GPIO.LOW)
		for i in range (0,4):
			GPIO.output(pin,GPIO.HIGH)
			sleep(.3)
			GPIO.output(pin,GPIO.LOW)
			sleep(.3)
	elif(pin==11):
		GPIO.output(7, GPIO.LOW)
		for i in range (0,4):
			GPIO.output(pin,GPIO.HIGH)
			#GPIO.output(11,GPIO.LOW)
			sleep(.3)
			GPIO.output(pin, GPIO.LOW)
			sleep(.3)
	else:
		for i in range (0,5):
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			sleep(.3)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(11,GPIO.LOW)
			sleep(.3)
		        #print "warning!!"	
                GPIO.output(7,GPIO.LOW)
                GPIO.output(11,GPIO.LOW)
	return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11,GPIO.LOW)
GPIO.output(7,GPIO.LOW)
#GPIO.cleanup()
#ser.write(b'1')
#blink(10)
#TestCase 1 - Object Avoidance
if testCase == 1:
	while True:
                line = ser.readline()
                print line
		if(int(line.strip()[0:len(line)-1]) < 5):
                        blink(10)
#TestCase 2 - Lane Changing - right
elif testCase == 2:	
        sleep(1)
        ser.write(b'1')
        sleep(2)
	thread.start_new_thread(blink,(7,))
        ser.write(b'2')
	sleep(1)
	ser.write(b'1')
#TestCase 3 - Lane Changing - left
elif testCase == 3:        
        sleep(1)
        ser.write(b'1')
        sleep(2)
	thread.start_new_thread(blink,(11,))
        ser.write(b'3')
	sleep(1)
	ser.write(b'1')
