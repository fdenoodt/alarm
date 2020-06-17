from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()
camera.resolution = (640, 480)
camera.start_preview()

i = 0
while(True):
    sleep(2 * 60)
    i = i + 1
    
    now = datetime.datetime.now()
    d = "{}_{}_{}_{}_{}_{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    camera.capture('/home/pi/Desktop/retrieve data/image{}_{}.jpg'.format(i, d))
    
camera.stop_preview()