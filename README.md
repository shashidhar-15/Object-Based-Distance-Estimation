# 📏 Real-Time Distance Estimation using YOLO & Monocular Camera

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red)
![Status](https://img.shields.io/badge/Status-Working-success)

---

## 🚀 Project Overview

This project implements a **real-time distance estimation system** using a single camera and computer vision techniques. By combining **YOLOv8 object detection** with basic camera geometry, the system estimates how far an object (bottle) is from the camera.

Unlike traditional systems that use ultrasonic or LiDAR sensors, this solution relies **purely on image processing**, making it low-cost and easy to deploy.

---

## 🎯 Key Features

* 🎥 Real-time video processing
* 🤖 Accurate object detection using YOLOv8
* 📦 Bottle detection (COCO dataset class)
* 📏 Live distance calculation
* ⚡ Lightweight and fast implementation
* 🖥️ Works on Windows with a standard webcam

---

## 🧠 How It Works

The system uses the formula:

```
D = (f × H) / h
```

Where:

* **D** → Distance from camera (meters)
* **f** → Focal length (pixels, obtained via calibration)
* **H** → Real-world object height (meters)
* **h** → Object height in image (pixels)

### 🔍 Process:

1. Capture video using OpenCV
2. Detect bottle using YOLOv8
3. Extract bounding box height in pixels
4. Apply formula to compute distance
5. Display distance in real-time

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **Ultralytics YOLOv8**
* **NumPy**

---

## 📂 Project Structure

```
├── detection.py        # Main script (YOLO + distance estimation)
├── yolov8n.pt         # YOLO model (auto-download or manual)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies

```
pip install ultralytics opencv-python numpy
```

### 3️⃣ Run the project

```
python detection.py
```

---

## 📐 Calibration (Important!)

Before using the system, you must calibrate your camera.

### Steps:

1. Place the object (bottle) at a known distance (e.g., **1 meter**)
2. Run detection and note pixel height (**h**)
3. Calculate focal length:

```
f = (D × h) / H
```

4. Update `FOCAL_LENGTH` in the code

---

## 🎥 Expected Output

* Camera window opens
* Bottle gets detected with bounding box
* Distance displayed above the object

Example:

```
0.85 m
```

---

## ⚠️ Limitations

* Requires known object size
* Accuracy depends on calibration
* Sensitive to lighting and camera angle
* Works best within **0.5m – 2m range**

---

## 🔮 Future Improvements

* 📦 Multi-object tracking
* 🎯 Custom-trained detection model
* 🧠 Depth estimation (no object size required)
* 📊 Data logging and analytics
* 🔌 Embedded system integration (ARM Cortex, Raspberry Pi)

---

## 📌 Applications

* Robotics navigation
* Obstacle detection
* Smart surveillance
* Assistive vision systems
* Low-cost measurement tools

---

## 🙌 Acknowledgements

* Ultralytics YOLOv8
* OpenCV Community
* COCO Dataset

---

## ⭐ Support

If you found this useful:

* ⭐ Star the repo
* 🍴 Fork it
* 🛠️ Improve it

---

## 📧 Contact

Feel free to reach out for collaboration or improvements!

---

✨ *This project showcases how powerful computer vision can be in solving real-world problems using just a camera.*
