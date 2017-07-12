
# IoT Drowsiness Detection using Computer Vision 

* Seattle Interactive 2016 T-Mobile Hackathon
 * Finalist for real time drowsiness detection using embedded computer vision. 
 * Scalable deployment through Resin.io and Docker 


## Design principles

### Engineering
  
  * Agile development - patches and updates pushed with Resin.io
  * Reslient to network or power loss, system crash
  * Scalability, mass deployable from inception
  * Leverage distributed in-memory storage and pub-sub 
  * Embedded computer vision and neural nets - working in 'the fog' as opposed to the cloud
  
### Philosophical
 * Flexible IoT platform for general-purpose computer vision and emotiove computing applications
 * Simple UX, supporting various user engagement styles
 * The 'anti-app': an unobstrustive 'enchanted' object' that facilitates a utility or experience. 
 * Anticipatory embrace of [emerging trends in tech] (http://na2.www.gartner.com/imagesrv/newsroom/images/emerging-tech-hc-2016.png;wa59f7b006c484099e): affective computing, IoT, distributed computing, quantified self, deep neural networks.




## Real time drowsiness detection

### Step 1
IR cam capture, face detection, image cropping

![Alt text](/images/snapcrop.jpg?raw=true "So tired..") 

### Step 2
Facial landmark identification, keypoint anaylsis, time weighted feedback, update frequency ~3 seconds

![Alt text](/images/alert.jpg?raw=true "alert!") 


## Real time mood insights (in progress)

Embedded insights using FaceNet in TensorFlow, trained on 37,000 images.

Live interactive user analytics using D3.js, supported by Kakfa and MemSQL and Spark

Attractive, unobtrusive real time form factor with live RGB feedback.


## Deployment

Resin.io

## Use


Device starts capture and analysis automatically when activated. Streaming logs viewable from console, most recent images viewable on local network image with data markup available via localhost:80

```bash 
resin ssh

cd raspiviz && python executor.py
```

Real time analytical data stream on SSH: timestamped drowsiness metrics & interpretation



#### TODO
  * Deploy TensorFlow model on device (model trained, deployment in progress)
  * Scalable and distributed pub-sub server using Kakfa (in progress) and in-memory datastore (MemSQL) and analytics (Spark)
  * Frontend user interactive visual analytics web client (in progress) 
  * Native device feedback on local desktop light



## License 
Apache License 2.0.
