import lights, image_processing

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
    for i in range(4):
            
        #DIRECTLY OBTAINING PROCESSED LIVE FEED
        imagepath=image_processing.preprocess_image()

        #COMPUTING MATCH PERCENTAGE
        referencepath = ref_images_array[i]
        match_percentage = image_processing.compute_match_percentage(referencepath, imagepath)

        #USING MATCH PERCENTAGE TO DETERMINE DURATION OF SIGNAL AND SENDING IT TO MICROCONTROLLER
        duration=0 #default, change all the other durations/match criteria later
        if match_percentage<20:
            duration=6
        elif 20<=match_percentage<25:
            duration=4
        elif 25<=match_percentage<30:
            duration=3
        elif 30<=match_percentage<=100:
            duration=2
        print(f"The match percentage is {match_percentage}, so the green light will be on for {duration} seconds.")
        #SENDING DURATION FOR TIME.STOP
        def run():
            return duration

        #RUNNING LEDS ACCORDINGLY
        lights.light_on(i+1) #CHECK WHETHER i OR i+1
        lights.wait(duration)
        lights.light_off(i+1)

        #LOOPING ENDS HERE