# Hand Gesture Controlled IoT Car

An IoT-based robotic car controlled entirely through real-time hand gestures using computer vision and AI.
This project was built during our 4th semester and combines Python, OpenCV, MediaPipe, WebSockets, and embedded systems to create a touchless robotic control experience.

The goal was simple:
Control a moving car using only hand gestures captured through a webcam — no physical remote, no buttons, just natural hand movement.

## Project Overview

The system uses a webcam to capture hand movements in real-time.
Using MediaPipe and OpenCV, gestures are detected and interpreted into commands like:

* Forward
* Backward
* Left
* Right
* Stop

These commands are then transmitted wirelessly through WebSockets to an ESP32/NodeMCU, which controls the motors of the robotic car.

This project combines:

* Computer Vision
* IoT
* Real-time Communication
* Embedded Systems
* Web-based Control Interface

## Features

### Gesture-Based Car Control

* Real-time hand gesture recognition
* Smooth directional control
* Touchless interaction system

### Computer Vision System

* Hand tracking using MediaPipe
* Real-time video frame processing with OpenCV
* Gesture detection through Python

### IoT Communication

* WebSocket-based communication
* ESP32/NodeMCU command handling
* Wireless control system

### Web-Based GUI

* Login interface
* Step-by-step setup guide
* Start/stop gesture recognition
* User-friendly control flow

## Tech Stack

### Software

* Python
* OpenCV
* MediaPipe
* WebSockets
* HTML
* CSS
* JavaScript

### Hardware

* ESP32 / NodeMCU
* L298N Motor Driver
* DC Motors
* Robotic Car Chassis
* Webcam

## System Workflow

1. Webcam captures hand gestures
2. Python processes frames using OpenCV
3. MediaPipe detects hand landmarks
4. Gesture is identified
5. Command is sent through WebSocket
6. ESP32 receives the command
7. Motor driver controls the car movement

## Supported Gestures

| Gesture     | Action   |
| ----------- | -------- |
| Open Palm   | Stop     |
| Thumb Up    | Forward  |
| Thumb Down  | Backward |
| Thumb Left  | Left     |
| Thumb Right | Right    |

## Project Structure

```bash id="p0j7aa"
project/
│
├── gesture_detection/
├── esp32_code/
├── web_interface/
├── static/
├── templates/
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash id="9uj7qk"
git clone <your-repository-link>
cd hand-gesture-iot-car
```

### Install Python Dependencies

```bash id="0z0joo"
pip install -r requirements.txt
```

### Run Gesture Detection

```bash id="91m2ki"
python gesture_control.py
```

### Upload ESP32 Code

* Open Arduino IDE
* Connect ESP32/NodeMCU
* Upload the provided firmware

### Start the Web Interface

```bash id="m2io9q"
python manage.py runserver
```

## Screenshots

Add project screenshots or demo images here.

Example:

```md id="2xsm6g"
![Gesture Detection](images/gesture.png)
![IoT Car](images/car.jpg)
```

## Future Improvements

Some ideas planned for future upgrades:

* Mobile app integration
* FPV camera streaming
* AI-based gesture customization
* Voice + gesture hybrid control
* Obstacle detection
* Autonomous navigation mode
* Better gesture accuracy using deep learning

## Learning Outcomes

This project helped us explore:

* Computer Vision concepts
* Real-time gesture recognition
* IoT communication systems
* Embedded hardware integration
* WebSocket communication
* AI-powered interaction systems
* Team collaboration and leadership

## Real-World Applications

This type of system can potentially be used in:

* Assistive technology
* Robotics
* Smart mobility systems
* Industrial automation
* Touchless control systems
* Human-computer interaction research

## Project Status

Working prototype with future expansion plans.

## Feedback

Suggestions, improvements, and contributions are always welcome.

If you found this project interesting, feel free to star the repository.

---

Built with curiosity, experimentation, and a passion for combining AI with real-world hardware systems.
