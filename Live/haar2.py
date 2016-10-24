
# coding: utf-8

# In[4]:

import cv2
import os
import numpy as np


# In[3]:


class Cascade():
    ''' Defaults'''
    out_dir = '/Users/zae/Desktop/face_processing/out/'
    
    
    def __init__(self, pic, out_dir=out_dir, grow=10,downsample=43,multi=False,all_pics=False):
        # self.purge_dir()
        self.all_pics = all_pics
        self.grow = grow
        self.downsample = downsample
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        self.pic = pic
        self.path = self.pic.split('/')
        self.img = cv2.imread(self.pic)
        self.multi = multi
        self.save = True
        self.out_dir = out_dir

        
    def purge_dir(self):
        os.system('rm -r  ~/Desktop/face_processing/out/')
        os.system('mkdir  ~/Desktop/face_processing/out/')

    def contrast_boost(self,img):
        hist,bins = np.histogram(img.flatten(),256,[0,256])
        cdf = hist.cumsum()
        cdf_m = np.ma.masked_equal(cdf,0)
        cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
        cdf = np.ma.filled(cdf_m,0).astype('uint8')
        img = cdf[img]
        return img
    
    def prime_face(self): 
        big_h = 0
        i = 0
        for (x,y,w,h) in self.faces:
            i += 1
            if h > big_h:
                big_h = h
                prime = i
        return prime
    
    def get_faces(self,multi=0):
        grow = self.grow
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.gray = self.contrast_boost(self.gray)
        #orig
        self.faces = self.face_cascade.detectMultiScale(self.gray, 1.3, 5)


        if self.multi:
            faces = self.faces[self.prime_face()]
        else: faces = self.
        for (x,y,w,h) in faces:
            size = (h,w)
            print size
            x1 = x-grow
            x2 = x+w+grow
            y1 = y-grow
            y2 = y+h+grow

            self.gen_out([x1,x2,y1,y2],self.img)
                        
    def gen_out(self,coords,inpic):
        
        # print "Extracting Face"
        downsample = self.downsample
        x1,x2,y1,y2 = coords
        face = cv2.rectangle(inpic,(x1,y1),(x2,y2),(255,255,0),0)
        #self.gray_normal = self.gray[y1:y2, x1:x2]
        #self.gray_boosted = self.contrast_boost(self.gray_normal)
        color_normal = face[y1:y2, x1:x2]
        # self.gray_boost_final = cv2.resize(self.gray_boosted,(downsample,downsample))
        if self.save==True:
            self.write(self.gray_boosted)


        # if self.all_pics:
        #     gray_final = cv2.resize(gray_normal,(downsample,downsample) )
        #     color_normal = face[y1:y2, x1:x2]
        #     self.gray_boosted = gray_boosted
        #     color_boosted = self.contrast_boost(color_normal)
        #     color_final = cv2.resize(color_normal,(downsample,downsample))
        #     color_boost_final = cv2.resize(color_boosted,(downsample,downsample))
        #     self.write(self.gray_boost_final)

        
    def get_eyes(self):
        self.save = False
        self.get_faces()
        eye_cascade = cv2.CascadeClassifier('parojosG.xml')#'haarcascade_eye_tree_eyeglasses.xml')#'haarcascade_eye.xml')#''
        eyes = eye_cascade.detectMultiScale(self.gray_boosted)
        grow = 0
        ct = 0
        for (ex,ey,ew,eh) in eyes:
            ct+=1
            eye = cv2.rectangle(self.gray_boosted,(ex,ey),(ex+ew,ey+eh),(0,255,0),0)
            x1 = ex-grow
            x2 = ex+ew+grow
            y1 = ey-grow
            y2 = ey+eh+grow
            eye = eye[y1:y2, x1:x2]
            self.write(eye,'_e'+str(ct))
        
    def write(self,outpic, extra=''):
        src = self.path[-1].split('.jpg')[0]
        out_dir = self.out_dir
        

        cv2.imwrite(os.path.join(out_dir + src + extra + '.jpg'),outpic) 




