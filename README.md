
# IoT Mood Insights using Computer Vision and Deep Learning

* Seattle Interactive 2016 T-Mobile Hackathon finalist.
* Real time drowsiness detection and face metrics using embedded computer vision. 
* Mood recognition in real time with embedded neural networks in TensorFlow (WIP - to be finished by 11/15)
* Scalable deployment through Resin.io and Docker 
* Scalable and fault tolerant backend using Kafka and MemSQL
* Interactive analytics service using PySpark backend with D3.js dashboards (in development)
* Robust IoT security practices leveraging distributed Cyprography via Apache Milagro 


## Design principles
 
  * Inexpensive product
  * Robust fault tolerance - recover from network or power loss, system crash
  * Scalability, mass deployable from inception
  * Leverage distributed in-memory storage and pub-sub 
  * Embedded computer vision and neural nets - working in 'the fog' as opposed to the cloud
  * Flexible IoT platform for emotion recognition applications
  * The 'anti-app': an unobstrustive 'enchanted' object' that facilitates a utility or experience. User can engage as much or little as they like and still have a positive experience
  * Anticipatory embrace of [emerging trends] (http://na2.www.gartner.com/imagesrv/newsroom/images/emerging-tech-hc-2016.png;wa59f7b006c484099e) in tech: affective computing, IoT, distributed computing, quantified self, deep neural networks.




## Real time drowsiness detection

### Step 1
IR cam capture, face detection, image cropping

![Alt text](/images/snapcrop.jpg?raw=true "So tired..") 

### Step 2Facial landmark identification, keypoint anaylsis, time weighted feedback, update frequency ~3 seconds

![Alt text](/images/alert.jpg?raw=true "alert!") 


## Real time mood insights (work in progress)

Embedded insights using FaceNet in TensorFlow, trained on 37,000 images.

Secure interactive user analytics using D3.js

Attractive, unobtrusive real time visualization with RBG desktop light.


## Deployment

Resin.io

## Use


Device starts capture and analysis automatically when activated. Streaming logs viewable from console, most recent images viewable on local network image with data markup available via localhost:80

```bash 
resin ssh

cd raspiviz && python executor.py
```

Real time analytical data stream on SSH: timestamped drowsiness metrics & interpretation



## Critical Path

### MVP
  * Deploy TensorFlow model on device (model trained, deployment in progress)
  * Scalable and distributed pub-sub server using Kakfa (in progress) and in-memory datastore (MemSQL) and analytics (Spark)
  * Frontend user interactive visual analytics web client (in progress) 
  * Native device feedback on local desktop light
  
### Longer term
  * beyond LAN: 3G + GPS connectivity with particle.io
  * Security with Apache Milagro distributed cytography


## License 
Apache License 2.0.
