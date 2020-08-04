from picamera import PiCamera
from database.DataBase import DataBaseAccess
from Color.Color import Color
import RPi.GPIO as GPIO
import time

GPIO_PIR = 11
#GPIO_LED = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIR, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(GPIO_LED, GPIO.OUT)        #LED output pin

print("PIR Module Test - Press CTRL-C to exit")
Current_State  = 0
Previous_State = 0

db = DataBaseAccess()
camera = PiCamera()

try:
	print("Waiting for PIR to settle ...")

	# Loop until PIR output is 0
	while GPIO.input(GPIO_PIR)==1:
		Current_State  = 0
	print("  Ready")
	c = Color("Hue_2")
	data = "0,0,0"
	c.postData(data)

  	# Loop until users quits with CTRL-C
	while True :
		#c = Color("Hue_2");
		#data = "0,0,0"
		#c.postData(data)
		# Read PIR state
		Current_State = GPIO.input(GPIO_PIR)
		if Current_State==1 and Previous_State==0:
			# PIR is triggered
			print("  Motion detected!")
			#GPIO.output(GPIO_LED, True)
			# Record previous state
			Previous_State=1
			camera.start_preview()
			time.sleep(5)
			camera.capture('/tmp/picture.jpg')
			camera.stop_preview()
			db.insertBLOB("/tmp/picture.jpg")
			data="100,100,100"
			#c = Color("Hue_2");
			#c.updateValue()
			c.postData(data)
			c.insertDB()
			time.sleep(5)
			data="0,0,0"
			c.postData(data)
			#c.updateValue()
			c.insertDB()
		elif Current_State==0 and Previous_State==1:
			# PIR has returned to ready state
			print("  Ready")
			#GPIO.output(GPIO_LED,False)
			Previous_State=0

		# Wait for 10 milliseconds
		time.sleep(0.01)

except KeyboardInterrupt:
	db.readBLOB("/home/pi/Desktop/picture");
	print("  Quit")
	# Reset GPIO settings
	GPIO.cleanup()



