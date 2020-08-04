from picamera import PiCamera
from database.DataBase import DataBaseAccess
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin = 16
GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

db = DataBaseAccess()
camera = PiCamera()

try:
	while(1):
		if GPIO.input(pin)==0:
			file_name = "/tmp/button/"+str(datetime.now())+".png"
			print("Button is pressed")
			camera.start_preview()
			camera.capture(file_name)
			#db.insertBLOB("/tmp/picture.jpg")
			camera.stop_preview()

except KeyboardInterrupt:
	#db.readBLOB("/home/pi/Desktop/picture")
	print("  Quit..")
	GPIO.cleanup()


