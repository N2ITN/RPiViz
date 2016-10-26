
# RPiViz

Drowsiness detection in real time using computer vision. Alerts can be send via GET requests
Seattle Interactive 2016 T-Mobile Hackathon finalist
Work in progress - massive feature additions on the way.


## install notes
Tested on Raspian Jesse Pixel
dlib is very slow to install, and pushes the limits of RPi memory!
dlib install will only work in headleess mode with GPU memory set to 64  (use ``` raspi config ``` )

#### Run locally in RPiViz folder:
```bash
sudo apt-get update
sudo apt-get install libopencv-dev python-opencv
sudo cat requirements.txt | xargs pip install
sudo apt-get install libboost-python-dev
sudo pip install dlib==19.1.0
curl -o ~/shape_predictor_68_face_landmarks.dat http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 | bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
```


#### Pip
pip package to automate installation of all dependencies currently in development.
Likely not 100% functional. 
Testing in progress!

* ``` sudo raspi config ```
  * command line boot
  *  gpu memory to 64 MB
  * accept reboot prompt
* ``` pip install RPiViz ```



Apache License 2.0.
