
## 📷 Screen to Virtual Webcam

![python](https://img.shields.io/badge/python-3.8+-blue.svg)
[![mss](https://img.shields.io/badge/mss-6.1.0-green.svg)](https://github.com/BoboTiG/python-mss)
[![pyvirtualcam](https://img.shields.io/badge/pyvirtualcam-0.8.0-brightgreen.svg)](https://github.com/letmaik/pyvirtualcam)
![portable](https://img.shields.io/badge/portable-windows%20x64-yellow.svg)
![license](https://img.shields.io/badge/license-GPL%20%28inherited%29-blueviolet.svg)

Python script bridging the stream from screen to virtual webcam.


### 📽️ Demo

| using Android's camera as PC's webcam (with the help of [scrcpy tool](https://github.com/Genymobile/scrcpy)) |
| :-: |
| <img src="/imgs/FromAndroid.gif?raw=true"> |

| using real-time game character as PC's webcam |
| :-: |
| <img src="/imgs/FromGame.gif?raw=true"> |

| using online/offline video as PC's webcam |
| :-: |
| <img src="/imgs/FromVideo.gif?raw=true"> |


### 🕹️ Get Started

#### 0️⃣ Install Supported Virtual Cameras

Follow the [guides suggested by pyvirtualcam](https://github.com/letmaik/pyvirtualcam#supported-virtual-cameras), or the steps below (will install [UnityCapture](https://github.com/schellingb/UnityCapture#installation) for Windows):

| Step | Description |
| :-: | :- |
| #1 | download and unzip [ScreenToVirtualcam.zip](https://github.com/der3318/screen-to-virtualcam/releases/download/2021.11.21/ScreenToVirtualcam.zip) |
| #2 | run `UnityCapture/Install/Install.bat` in admin console to register the DirectShow Filter to be available in Windows programs |


#### 1️⃣ Start Streaming

Using Portable Version (Windows 10/11 AMD64)

| Step | Description |
| :-: | :- |
| #1 | download and unzip [ScreenToVirtualcam.zip](https://github.com/der3318/screen-to-virtualcam/releases/download/2021.11.21/ScreenToVirtualcam.zip) |
| #2 | run `launch.bat` and input preferred parameters |
| #3 | select `Unity Video Capture` (or other vcam) from the apps using webcam |

Using Python Interpreter

| Step | Description |
| :-: | :- |
| #1 | install python3 |
| #2 | pip-install the dependencies listed in `requirements.txt` (e.g., mss, Pillow, opencv-python, opencv-python, rich) |
| #3 | invoke `screen2vcam.py` with preferred parameters |
| #4 | select `Unity Video Capture` (or other vcam) from the apps using webcam |


#### 2️⃣ Uninstall

| Step | Description |
| :-: | :- |
| #1 | run `UnityCapture/Install/Uninstall.bat` in admin console to unregister |
| #2 | simply remove all the unzipped binaries |
