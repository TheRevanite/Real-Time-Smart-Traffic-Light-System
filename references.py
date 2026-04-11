import camera_capture, servomotor, os, time

for i in range(1, 5):
        if i%2==0: 
            servomotor.roads2(3)
        else:
            servomotor.roads1(3)
        print(f"Capturing reference image {i}.")
        if i == 1 or i == 4:
            frame1 = camera_capture.capture_camera1()
            os.rename(frame1, f'og_reference{i}.jpg')
            time.sleep(2)      
        elif i == 2 or i == 3:
            frame2 = camera_capture.capture_camera2()
            os.rename(frame2, f'og_reference{i}.jpg')
            time.sleep(2)