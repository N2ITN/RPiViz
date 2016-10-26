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

# Load in main script to reduce disk IO
predictor = dlib.shape_predictor(
    "/home/pi/Desktop/shape_predictor_68_face_landmarks.dat"
)  #Landmark identifier. Set the filename to whatever you named the downloaded file

# Camera rotation and resolution options
#nv.rotation = 180
#nv.resolution = (480, 360)
#nv.resolution = (960, 540)
#nv.resolution = (1280, 720)
#nv.resolution = (1920, 1080)
nv.resolution = (2592,1944)

# TODO: Remove code for local network alerts
'''
try:
    requests.get('http://192.168.43.45:3000/fan/off')
    requests.get('http://192.168.43.45:3000/lght/off')
except Exception as e:
    print e
'''
print "starting"
#@profile
def camera_loop(loops, nap):
    """ Orchestrator of all """
    buffer = []
    for loop in xrange(0, loops):
        snap = '/home/pi/Desktop/snap.jpg'
        start = time()
        nv.capture(snap)
        cal = .370

        # TODO: Function here
        try:
            shape, frame = crop2face(snap, predictor)
        except TypeError:
            continue
        analysis = do_magic.analyze(shape, frame)
        print start - time(), "finished analysis"
        if not analysis:
            print "no face detected"
            continue
        perc_asleep = round((analysis / cal) * 100, 2)

        # TODO: Function
        buffer.append(perc_asleep)
        print buffer
        a = False
        vector = int(np.mean(buffer))
        defcon = (255, 255, 255)
        alertness = 'calibrating'

        # TODO: Functionalize as "alert", create option for network alert or preview window
        if len(buffer) > 1:
            try:
                if int(vector) > 85:
                    defcon = (0, 255, 0)
                    alertness = 'excellent'
                    #requests.get('http://192.168.43.45:3000/fan/off')
                    #requests.get('http://192.168.43.45:3000/lght/off')

                elif int(vector) > 75:
                    alertness = 'okay'
                    #requests.get('http://192.168.43.45:3000/fan/on')
                    #requests.get('http://192.168.43.45:3000/lght/on')
                    #requests.get('https://wt-dev-screenverve_com-0.run.webtask.io/internetButton?webtask_no_cache=1')
                    defcon = (0, 255, 255)
                else:
                    defcon = (0, 0, 255)
                    alertness = 'danger zone'
                    #requests.get('http://192.168.43.45:3000/buzz/on')
                    sleep(2)
                    #requests.get('http://192.168.43.45:3000/buzz/off')
                    a = True
            except Exception as e:
                print e
            buffer.pop(0)
            print alertness
    
    # TODO: Functionalize as "preview_window"
        text = ' '.join(['ratio', str(analysis)])
        text2 = ' '.join(['alertness:', alertness])  #, str(vector)])
        cv2.destroyAllWindows()
        img = cv2.imread("snap_draw.jpg")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text2, (10, 30), font, .5, defcon, 1, cv2.CV_AA)
        if a:
           cv2.putText(img, 'sending ALERT', (10, 50), font, .5, (0, 0, 255),
                        1, cv2.CV_AA)
        cv2.namedWindow('z', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('z', cv2.WND_PROP_FULLSCREEN,
                              cv2.cv.CV_WINDOW_FULLSCREEN)
        cv2.imshow('z', img)
        cv2.imwrite('alert.jpg',img)
        cv2.waitKey(1000)
    
    print time() - start, 'total seconds'
    print
    print


camera_loop(10, 0)
