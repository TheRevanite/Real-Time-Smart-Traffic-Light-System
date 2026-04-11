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


def capture_camera2():
            picam2 = Picamera2(1)

            config = picam2.create_still_configuration() # sets up default parameters optimized for taking single, high-quality images
            picam2.configure(config) 

            picam2.start()
            sleep(2)
            picam2.start_and_capture_file("new_image.jpg")

            picam2.close()
            
            return "new_image.jpg"