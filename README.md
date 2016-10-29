
# RPiViz

* Drowsiness detection in real time using computer vision. IoT connected alerts.
* Seattle Interactive 2016 T-Mobile Hackathon finalist.
* Work in progress - massive feature additions on the way.

## Real time drowsiness detection

IR cam capture, face detection, image cropping


![Alt text](/images/snapcrop.jpg?raw=true "So tired..") 

Facial landmark identification, keypoint anaylsis, time weighted feedback, update frequency ~3 seconds


![Alt text](/images/alert.jpg?raw=true "alert!") 


## Design principles
 
  * inexpensive
  * robust fault tolerance - recoverable with network, power loss, system crash
  * mass deployable
  * data processing on device, 'the fog' as opposed to the cloud
  * flexible IoT platform for emotion recognition applications
  * 'anti-app': an unobstrustive 'enchanted' object' that facilitates a utility or experience 

## Deployment

Resin.io

## Use

```bash 
resin ssh

cd raspiviz && python executor.py
```

Most recent images viewable on local network
Real time analytical data stream on SSH: timestamped drowsiness metrics & interpretation



## Next steps

  * logging, native sqlite store, web based dashboard & d3 visualization
  * native device alerts
  * beyond LAN: 3G + GPS connectivity with particle.io
  * apache milagro distributed cytography (in progress)
  * tensorflow for deeper emotive analysis (in progress)


## License 
Apache License 2.0.
