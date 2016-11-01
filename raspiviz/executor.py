""" main loop """

from picamera import PiCamera
from time import sleep, time
import do_magic
from identify import crop2face
import numpy as np
import cv2
import requests
nv = PiCamera()
import dlib
import os
import sh
from time import ctime

# p = __file__
# # Load in main script to reduce disk IO
# p = os.path.dirname(os.path.realpath(__file__))

target = os.path.join("shape_predictor_68_face_landmarks.dat")
predictor = dlib.shape_predictor(target)

#Landmark identifier. Set the filename to whatever you named the downloaded file

# Camera rotation and resolution options
nv.rotation = 180
#nv.resolution = (480, 360)
#nv.resolution = (960, 540)
#nv.resolution = (1280, 720)
nv.resollution = (1296,480)
#nv.resolution = (1920, 1080)
#nv.resolution = (2592,1944)

# TODO: Remove code for local network alerts
'''
try:
    requests.get('http://192.168.43.45:3000/fan/off')
    requests.get('http://192.168.43.45:3000/lght/off')
except Exception as e:
    print e
'''
print("starting")


#@profile
def camera_loop(show=False):
    """ Orchestrator of all """
        
    def get_analysis():
        """ call CV libraries"""
        try:
            shape, frame = crop2face(snap, predictor)
        except TypeError:
            return None
        analysis = do_magic.analyze(shape, frame)
        print 
        if not analysis:
            print("no face detected")
            return None
        perc_asleep = round((analysis / cal) * 100, 2)
        return [analysis, perc_asleep]


    def image_out():
        text = ' '.join(['ratio', str(analysis)])
        text2 = ' '.join(['alertness:', alertness])  #, str(vector)])
        cv2.destroyAllWindows()
        img = cv2.imread("snap_draw.jpg")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text2, (10, 30), font, .5, defcon, 1, cv2.CV_AA)
        if a:
            cv2.putText(img, 'sending ALERT', (10, 50), font, .5, (0, 0, 255),
                        1, cv2.CV_AA)
            if show == True:
                cv2.startWindowThread()
                cv2.namedWindow('z', cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty('z', cv2.WND_PROP_FULLSCREEN,
                                        cv2.cv.CV_WINDOW_FULLSCREEN)
                cv2.imshow('z', img)
                cv2.waitKey(1000)
        cv2.imwrite('alert.jpg', img)

    buffer = []
    cal = 1
    calibrator = []
    calibrating = True
    while True:
        snap = 'snap.jpg'
        start = time()
        nv.capture(snap)
        # TODO: Function

        alertness = 'calibrating'

        # TODO: Functionalize as "alert", create option for network alert or preview window
        if calibrating == True:
            cal_len = len(calibrator)
            if cal_len < 5:
                print 'calibrating, show neutral awake face'
                res = get_analysis()
                if res:
                    analysis, perc_asleep = res
                else: continue 

                calibrator.append(perc_asleep)
            elif len(calibrator) == 5:
                cal = np.mean(calibrator)
                calibrating = False

        else:
            res = get_analysis()
            if res:
                analysis, perc_asleep = res
            else: continue
            
            buffer.append(perc_asleep)
            print(buffer)
            a = False
            vector = np.mean(buffer)
            print(vector)
            defcon = (255, 255, 255)
            try:
                if vector > 0.85:
                    defcon = (0, 255, 0)
                    alertness = 'excellent'
                    #requests.get('http://192.168.43.45:3000/fan/off')
                    #requests.get('http://192.168.43.45:3000/lght/off')

                elif vector > 0.75:
                    alertness = 'okay'
                    #requests.get('http://192.168.43.45:3000/fan/on')
                    #requests.get('http://192.168.43.45:3000/lght/on')
                    #requests.get('https://wt-dev-screenverve_com-0.run.webtask.io/internetButton?webtask_no_cache=1')
                    defcon = (0, 255, 255)
                else:
                    defcon = (0, 0, 255)
                    alertness = 'danger zone'
                    #requests.get('http://192.168.43.45:3000/buzz/on')
                    #sleep(2)
                    #requests.get('http://192.168.43.45:3000/buzz/off')
                    a = True
            except Exception as e:
                print(e)
            if len(buffer) > 10:
                buffer.pop(0)
            print(ctime())
            print(alertness)
            print()
            image_out()
            

def start():

    camera_loop()


start()
