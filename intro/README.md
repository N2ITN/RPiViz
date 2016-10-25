# Emotive IOT Lighting

## Goal
This is a personal project to build and IOT device that used motion recognition to detect  attention & focus vs distraction & tiredness, using TensorFlow on Raspberry Pi 3. The user's 'focus delta' will be translated to RGB colors and related to a wireless LED lamp for real time feedback. The anticipated use is facilitating a healthier approach to work hygiene, where tiredness and distraction can prompt short breaks to optimize productivity.
This issue has direct use for almost industry where a worker is sitting at a computer for prolonged periods of time.

The project is a work in progress and the road map below will be updated as it evolves. 
Code will be posted as it is developed, so far the work has been installing and configuring stock libraries, for which documentation already exists.

My primary goal is to learn through action in order to boost my machine learning and deep learning skills. The code will remain open source. 

If and when the completed prototype unit is succeeds at its task, I will consider a starting a Kickstarter to further product development. If there is sufficient interest in a final product, I will find others to help refine and iterate the design for MVP. If the final product is flawed, I still had a fun learning project. 

## Technical Overview

Pictures captured on the Pi's camera are analyzed by TensorFlow. Pictues will only be analyzed if openCV's Haar Cascaade can identify a face in the picutre.

The top layer of Google's Inceptionv3 model will be 'fine tuned' using hand-labeled images from Google images. The model can then be [quantized to 8-bit](https://petewarden.com/2016/05/03/how-to-quantize-neural-networks-with-tensorflow/) to reduce size and processing time.

If this cannot be made to produce satisfactory accuracy, plan B is as follows:
Train a new network on data from Kaggle's [Facial Emotion Recognition 2013](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data) contest. This data has been well studied and contains labels for 7 basic emotions.
The model will be fed new labeled data of face pictures showing attention vs inattention.
The resulting output vectors will be analyzed using PCA to find a single vector that predicts changes in attention, for which new inputs can be translated to.

These user's vigilance data will be mapped to color changes in a small desktop lamp. Users will be able to practice better work hygiene practices by taking intelligently timed breaks, as cues from the lamp will generated based on their attention deltas, and calibrated using academic studies of ideal break intervals.

Additionally, the resulting output vectors will be logged in a cloud database, where users may view their personal data using interactive web frameworks such as D3 in addition to anonymized  group data.

Another potential edition is using a network such as the [MIT places model](https://github.com/metalbubble/places365) to locate which type of room the user is in, and track the relationship between productivity and space, for both single user accounts and global data. This could drive insights into the working environments which facilitate the longest and most consistent levels of concentration.

# Completed Tasks:

### Scope and vision:

  Action-ready conceptual diagram based on domain research

### Acquire hardware:
 
  * NOIR Night Vision Camera
  
  * Rasberry Pi infrared receiver / transmitter  
  
  * RGB LED desktop light

### RPi Hardware

  * Set up Pi as headless SSH server
  
  * Test IR camera in varying lighting conditions

  * Overclock CPU to 1400 GHz, memory to 500
  
  * Activate dynamic GPU / RAM allocations
  
### RPi Software Config
  
  * Test openCV face tracking (Haar cascade)
  
  * Install and compare TensorFlow, Caffe
  
### Web server

  * Register domain name
  
  * Configure web hosting
  
  * Build website template
  
  
# In progress:

### Neural Network Calibration

  * Find, test accurate emotional recognition model
  
  * Evaluate accuracy for tired/attentive faces
  
  * Acquire/label images of tired/attentive faces for fine tuning
  
  * Test against emotive model
  
  * Use PCA in SKLearn to model accuracy on tired/attentive faces
  
  
# TODO:  
  
### IR Remote

  * Capture desktop RGB LED lamp color control signals from remote with RPi IR reciever board
  
  * Transmit color commands to lamp from Raspberry Pi 3
  
### Capture Test Data

  * Set camera to record snapshots at set intervals (as defined by the TensorFlow's throughput speed). Target ~= 30 seconds. Adjust as necessary.
  
  * Compare snapshots to model output for heuristic accuracy
  
  * Reiterate design

## Feedback engineering

  * Literature review of work hygiene, optimal break policy

  * Integrate findings into feedback model and include sources in documentation for attribution and theoretical support.
  
### Web Server Host
   
  * Write network protocols to SSH of protobuf'd Python dictionary objects

  * Implement redis database to record model output snapshots
  
  * Add DB interface with interactive D3 analytics suite
  
  
# Conceptual Design
  
![alt text](https://github.com/N2ITN/RPi3_Tensor_Emotive/blob/master/images/Neural%20Emotion%20-%20Neural%20Feels.jpg)

