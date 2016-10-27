#!/bin/bash
echo starting installation
echo installing opencv
sudo apt-get install libopencv-dev python-opencv
echo installing python requirements
sudo cat requirements.txt | xargs pip install
echo installing libboost-python-dev
sudo apt-get install libboost-python-dev
echo installing dlib, this will take a long time
sudo pip install dlib==19.1.0

