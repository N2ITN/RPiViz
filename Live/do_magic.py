import cv2
import dlib
import glob
import os
import numpy
from time import time
picture_dir = ''
from identify import crop2face

def distance_2D (x1,y1,x2,y2):
		a = numpy.array((x1,y1))
		b = numpy.array((x2,y2))
		dist = numpy.linalg.norm(a-b)
		return dist

def analyze(shape,frame):
	start = time()
	print time() - start, 'dlib start'
        def array_maker(n1,n2):
        	return distance_2D(shape.part(n1).x, shape.part(n1).y, shape.part(n2).x,shape.part(n2).y)


	'''
	## OLD WAY
	detector = dlib.get_frontal_face_detector()
	img = cv2.imread(frame)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	clahe_image = clahe.apply(gray)
	detections = detector(clahe_image, 1) #Detect the faces in the image

	print time()-start, 'finished detections'
	print

	print type(detections)
	for k,d in enumerate(detections):
		print type(k) ,type(d)	
		print k, d


	print time() - start, 'finished detecting faces'
	exit()
	'''
	###



	# for k,d in enumerate(detections): #For each detected face
	# 	dete
	# 	exit()
	# shape = predictor(frame, detections) #Get coordinates		

	left_len = array_maker(36,39)
	left_open_top = array_maker(37, 41)
	left_open_bottom = array_maker(38,40)
	left_open = (left_open_top + left_open_bottom)/2.
	ratio_L =  (left_open / left_len) 
	ratio_L.round(1)

	right_len = array_maker(42,45)
	right_open_top = array_maker(43, 47)
	right_open_bottom = array_maker(44,46)
	right_open = (right_open_top + right_open_bottom)/2.
	ratio_R =  (right_open / right_len) 
	ratio_R.round(1)
	total_ratio = (ratio_R + ratio_L)/2

	for i in range(1,68): #There are 68 landmark points on each face
	# eyes: (36,48)
		cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (255,255,255), thickness=1) #For each point, draw a red circle with thickness2 on the original frame
        y1 = shape.part(8).y
        y2 = (shape.part(24).y + shape.part(19).y)/2
        x1 = shape.part(2).x
        x2 = shape.part(16).x

	print time() - start, 'dlib finish annotation'
	crop = frame[y2-60 : y1+30 ,x1-50 : x2+50 ]
	cv2.imwrite('snap_draw.jpg', crop)
	print time() - start, 'dlib finish image annotation + write'
	return total_ratio.round(4)



        '''
#        Save picture with points

        for i in range(1,68): #There are 68 landmark points on each face
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,0,255), thickness=2) #For each point, draw a red circle with thickness2 on the original frame
            print i+1, shape.part(i)
            y1 = shape.part(8).y
	    y2 = (shape.part(24).y + shape.part(19).y)/2
            x1 = shape.part(2).x
            x2 = shape.part(16).x

	print time() - start, 'dlib finish annotation'
	crop = frame[y2-60 : y1+30 ,x1-50 : x2+50 ]
        cv2.imwrite("allpoints" + ".jpg", crop)
        exit()
        '''


# 192.168.0.17:8000

        
