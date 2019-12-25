# MOOC Plagiarism Detection Multimodal System
A server application to detect the probability of plagiarism in realtime on the client's PC. It uses CV and ML algorithms to predict if the person attempting an online test is cheating or not using inputs through webcam, microphone, and screen recording.

# Modules:
1. Audio Detection
2. Screen Capture and Analysis
3. Face Orientation
4. Face Recognition


## Audio Detection
* Seprating noise and speaking sound.
* If speaking sound is more than 15% of the audio, then it is plag because the person is talking to someone.

## Screen Capture and Analysis
* Detecting if the person is stuck to the test/quiz page or opening anything else.
* Opening any thing else more than 5 seconds will be considered as plag.

## Face Orientation
Detects if the person giving the test is looking somewhere else (other than the computer's screen).

## Face Recognition
* Detects if the person sitting in front of the webcam and giving the test/quiz is the one who is supposed to give the test.
* It uses a photo of the authorized person to cross-check with the video from webcam.


