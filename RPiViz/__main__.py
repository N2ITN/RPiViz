import sys
from subprocess import call
import os
if sys.argv[1] == 'setup':
	deps.main()
elif sys.argv[1] == 'start':
        p = os.path.dirname(os.path.realpath(__file__))
        target = os.path.join(p,"shape_predictor_68_face_landmarks.dat.bz2")
        if not os.path.isfile(target):
                call(str('curl -o ' + target + ' http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2').split())
                call(str('bzip2 -d -k ' + target).split())
        import executor
	executor.start()
