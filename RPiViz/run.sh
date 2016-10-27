echo starting installation
echo installing opencv
sudo apt-get install libopencv-dev python-opencv
echo installing python requirements
sudo cat requirements.txt | xargs pip install
echo installing libboost-python-dev
sudo apt-get install libboost-python-dev
echo installing dlib, this will take a long time
sudo pip install dlib==19.1.0
echo downloading shape predictor
curl -o ~/shape_predictor_68_face_landmarks.dat http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 | bzip2 -d shape_predictor_68_face_landmarks.dat.bz2