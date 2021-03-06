""" Detect face with OpenCV, return DLib rectangle """

import cv2
import dlib
import numpy as np


# TODO: split into 2 functions, get_face, extract_data
#@profile
def crop2face(pic, predictor):
    """ Greyscale img, boost contrast, detect faces, extract coords from first face found, convert to dlib rectangle"""

    img = cv2.imread(pic)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))
    clahe_image = clahe.apply(gray)

    
    eq = cv2.equalizeHist(gray)  #<--- more drastic contrast boosting, doesn't work evenly across lighting conditions
    faceprime = face_cascade.detectMultiScale(clahe_image, 1.3, 5)

    # Convert face coords to rectangle corner points, grow rectangle to capture full face
    
    for (x, y, w, h) in faceprime:
        grow = h/10
        size = (h, w)
        x1 = x - grow
        x2 = x + w + grow
        y1 = y - grow
        y2 = y + h + grow

        
        # Convert to dlib rectangle datatype
        # detections = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
        # detections = dlib.rectangle(int(x), int(y), int(x2), int(y2))
        
        # Save cropped face img
        color_normal = img[y1:y2, x1:x2]
        cv2.imwrite('snapcrop.jpg', color_normal)
        

        # import test_points
        # test_points.circle(w,h)
        detections = dlib.rectangle(int(0), int(0), int(w), int(h))

        # blurred = cv2.GaussianBlur(clahe_image, (3, 3), 0)
        # tight = cv2.Canny(blurred, 225, 250)
        # wide = cv2.Canny(blurred, 10, 100)
        # Detect face landmarks with dlib rectangle, dlib shape predictor
        clahe_crop = clahe_image[y1:y2, x1:x2]
        eq1 = cv2.equalizeHist(clahe_crop)
        cv2.imwrite('clahe_crop.jpg', clahe_crop)
        cv2.imwrite('normal_eq.jpg', eq)
        cv2.imwrite('clahe_eq.jpg', eq1)

        #LBP_img = LBP.main(clahe_crop)
        shape = predictor(eq1, detections)
        return shape, eq1
