from picamera2 import Picamera2
from time import sleep

def capture_camera1():
            picam1 = Picamera2(0)

            config = picam1.create_still_configuration() # sets up default parameters optimized for taking single, high-quality images
            picam1.configure(config) 

            picam1.start()
            sleep(2)
            picam1.start_and_capture_file("new_image.jpg")

            picam1.close()
            
            return "new_image.jpg"