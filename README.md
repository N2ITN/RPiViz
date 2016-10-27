
# RPiViz

* Drowsiness detection in real time using computer vision. Alerts can be send via GET requests.
* Seattle Interactive 2016 T-Mobile Hackathon finalist.
* Work in progress - massive feature additions on the way.

## Real time drowsiness detection
![Alt text](/image_examples/alert.jpg?raw=true "So tired..")


## Install notes
* Tested on Raspian Jesse Pixel
* dlib is very slow to install, and pushes the limits of RPi memory!
* dlib install will only work in headless mode with GPU memory set to 64  (use ``` raspi config ``` )

### Bash:
```bash
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo apt-get install libopencv-dev python-opencv
git clone https://github.com/N2ITN/RPiViz.git
cd RPiViz/RPiViz
sudo cat requirements.txt | xargs pip install
sudo apt-get install libboost-python-dev
* ``` sudo raspi config ```
  * command line boot
  *  gpu memory to 64 MB
  * accept reboot prompt
sudo pip install dlib==19.1.0
curl -o ~/shape_predictor_68_face_landmarks.dat http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 | bzip2 -d shape_predictor_68_face_landmarks.dat.bz2

```



### Pip
forthcoming

## Run

``` python -m RPiViz```




## License 
Apache License 2.0.
