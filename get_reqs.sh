#!/bin/bash

set -o errexit
set -o pipefail
sudo apt-get update
sudo apt-get upgrade
sudo cat requirements.txt | xargs pip install
sudo apt-get install libopencv-dev python-opencv libboost-python-dev
sudo pip install dlib==19.1.0
python executor.py
