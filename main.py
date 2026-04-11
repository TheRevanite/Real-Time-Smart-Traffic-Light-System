import lights, image_processing, camera_capture, servomotor

#RUNNING PIN SETUP
pin_mappings=lights.setup()

#REFERENCE IMAGE PROCESSING (THIS ASSUMES THERE ARE ALREADY 4 RAW IMAGES BY THE AFOREMENTIONED NAMES)
og_ref_images = [
        "og_reference1.jpg",
        "og_reference2.jpg",
        "og_reference3.jpg",
        "og_reference4.jpg",
    ]
ref_images_array=image_processing.image_conversion(og_ref_images)

#INDEFINITE LOOPING HERE ONWARDS
while True:

    #LOOPING FOR EACH ROAD STARTS HERE 
    for i in range(1, 5):
        #ROTATING THE MOTOR ACCORDINGLY.
        servomotor.roads2(2)
            
        #DIRECTLY OBTAINING PROCESSED LIVE FEED
        if i == 1 or i == 4:
            frame1 = camera_capture.capture_camera1()
            imagepath=image_processing.preprocess_image(frame1)
        elif i == 2 or i == 3:
            frame2 = camera_capture.capture_camera2()
            imagepath=image_processing.preprocess_image(frame2)

        #COMPUTING MATCH PERCENTAGE
        referencepath = ref_images_array[i-1]
        match_percentage = image_processing.compute_match_percentage(referencepath, imagepath)

        #USING MATCH PERCENTAGE TO DETERMINE DURATION OF SIGNAL AND SENDING IT TO MICROCONTROLLER
        duration=0 #THE DEFAULT VALUE FOR DURATION IS SET AND UPDATED FURTHER IN THE CODE
        if match_percentage<20:
            duration=6
        elif 20<=match_percentage<25:
            duration=4
        elif 25<=match_percentage<30:
            duration=3
        elif 30<=match_percentage<=100:
            duration=2
        print(f"The match percentage is {match_percentage}, so the green light will be on for {duration} seconds.")
        if i%2==0: 
            servomotor.roads2(duration)
        else:
            servomotor.roads1(duration)
        #RUNNING LEDS ACCORDINGLY
        lights.light_on(i) #CHECK WHETHER i OR i+1
        lights.wait(duration)
        lights.light_off(i)

        #LOOPING ENDS HERE