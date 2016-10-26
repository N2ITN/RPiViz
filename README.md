
# RPiViz

Drowsiness detection in real time using computer vision. Alerts can be send via GET requests
Seattle Interactive 2016 T-Mobile Hackathon finalist
Work in progress - massive feature additions on the way.


## install notes
Tested on Raspian Jesse Pixel
dlib is very slow to install, and pushes the limits of RPi memory!
dlib install will only work in headleess mode with GPU memory set to 64  (use ``` raspi config `` )

#### Manual
```bash
sudo apt-get install libopencv-dev python-opencv
sudo pip install scipy, numpy
sudo apt-get install libboost-python-dev
pip install dlib
```

#### Pip
pip package to automate all of this is currently in testing



unzip into RPiViz folder:
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2




Apache License 2.0.
