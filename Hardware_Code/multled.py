import RPi.GPIO as GPIO
import time

# blinking function
def blink(pin):
	if(pin == 7):
		GPIO.output(11,GPIO.LOW)
		for i in range (0,10):
			GPIO.output(pin,GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(pin,GPIO.LOW)
			time.sleep(.5)
	elif(pin==11):
		GPIO.output(7, GPIO.LOW)
		for i in range (0,10):
			GPIO.output(pin,GPIO.HIGH)
			#GPIO.output(11,GPIO.LOW)
			time.sleep(.5)
			GPIO.output(pin, GPIO.LOW)
			time.sleep(.5)
	else:
		for i in range (0,10):
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(11,GPIO.LOW)
			time.sleep(.5)
		        print "warning!!"
	
	return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11,GPIO.LOW)
GPIO.output(7,GPIO.LOW)
print "Enter pin 7 or 11"
pin = raw_input()
fpin= int(pin)
'''for i in range(0,5):
        blink(7)
        blink(11) '''
blink(fpin)
GPIO.cleanup()
