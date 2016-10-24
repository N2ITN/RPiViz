import cv2
import dlib
import numpy as np
def crop2face(pic,predictor):
    img  = cv2.imread(pic)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)
    equ = cv2.equalizeHist(gray)
    faceprime = face_cascade.detectMultiScale(clahe_image, 1.3, 5)
    print faceprime
    grow = (30)
    for (x,y,w,h) in faceprime:
        size = (h,w)
        x1 = x-grow
        x2 = x+w+grow
        y1 = y-grow
        y2 = y+h+grow


        # frame = dlib.rectangle(long(x1), long(y1),long(x2), long(y2))
        # rects = dlib.rectangles(frame)
        # SO = np.array([long(x),long(y),long(x+w),long(y+h)])
        detections = dlib.rectangle(long(x),long(y),long(x+w),long(y+h))
        # for k,v in enumerate(rects):
        #     print k,v
        
        
        #color_normal = img[y1:y2, x1:x2]
        #cv2.imwrite('snapcrop.jpg',color_normal)
        shape = predictor(clahe_image, detections)
        print shape
        return shape, img



