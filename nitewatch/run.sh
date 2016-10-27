sudo apt-get update
sudo apt-get install libopencv-dev python-opencv
sudo cat requirements.txt | xargs pip install
sudo apt-get install libboost-python-dev
sudo pip install dlib==19.1.0
curl -o ~/shape_predictor_68_face_landmarks.dat http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 | bzip2 -d shape_predictor_68_face_landmarks.dat.bz2