import cv2

def preprocess_image(img_path):
    img = cv2.imread(img_path) #Read the original frame
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert to grayscale
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0) #Blur the image for better edge detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) #Canny Edge Detection
    cv2.imwrite("final_image.jpg", edges)

    return "final_image.jpg"

def preprocess_reference(img_path):
    img = cv2.imread(img_path) #Read the original frame
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert to grayscale
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0) #Blur the image for better edge detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) #Canny Edge Detection
    return edges

def image_conversion(og_ref_images):
    reference_edge1 = preprocess_reference(og_ref_images[0])
    cv2.imwrite("reference1.jpg", reference_edge1)
    reference_edge2 = preprocess_reference(og_ref_images[1])
    cv2.imwrite("reference2.jpg", reference_edge2)
    reference_edge3 = preprocess_reference(og_ref_images[2])
    cv2.imwrite("reference3.jpg", reference_edge3)
    reference_edge4 = preprocess_reference(og_ref_images[3])
    cv2.imwrite("reference4.jpg", reference_edge4)
    ref_images_array = [
        "reference1.jpg",
        "reference2.jpg",
        "reference3.jpg",
        "reference4.jpg",
    ]
    return ref_images_array

def compute_match_percentage(image1, image2):
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE) #Load images
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE) #Load images
    orb = cv2.ORB_create() #Initiate ORB detector
    kp1, des1 = orb.detectAndCompute(img1, None) #Find keypoints and descriptors
    kp2, des2 = orb.detectAndCompute(img2, None) #Find keypoints and descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) #Creating BFMatcher object
    matches = bf.match(des1, des2) #Match descriptors
    matches = sorted(matches, key=lambda x: x.distance) #Sort them in the order of their distance
    good_matches = [m for m in matches if m.distance < 50]  # Keep matches with distance < 50
    num_good_matches = len(good_matches) # Count good matches
    total_matches = len(matches) # Total matches found between the two images
    keypoints_ratio = min(len(kp1), len(kp2)) / max(len(kp1), len(kp2)) # Calculate the keypoints ratio to balance keypoints of varying images
    match_percentage = (num_good_matches / total_matches) * keypoints_ratio * 100 # Compute the final match percentage

    return match_percentage