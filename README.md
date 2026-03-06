# YOLOv8 Object Detection System

## 📌 Project Description

This project implements a **real-time Object Detection System using YOLOv8**.
The system can detect objects from **images, videos, and live webcam streams** using a pre-trained YOLOv8 model.

The application is developed in **Python using OpenCV and the Ultralytics YOLOv8 framework**.
It provides bounding boxes, object labels, and counts of detected objects.

---

## 🚀 Features

* Object detection using **YOLOv8 (Ultralytics)**
* Supports **three input types**

  * Image detection
  * Video detection
  * Webcam detection
* **Object counting** for each detected class

---

## 🛠️ Technologies Used

* **Python**
* **YOLOv8 (Ultralytics)**
* **OpenCV**
* **NumPy**

---

## 📂 Project Structure

```
Object-Detection/
│
├── main.py                # Main program to select input type
├── detect_image.py        # Object detection for images
├── detect_video.py        # Object detection for videos
├── detect_webcam.py       # Object detection using webcam
│
├── yolov8n.pt             # Pre-trained YOLOv8 model
├── requirements.txt       # Project dependencies
│
├── image.jpg              # Sample image
├── video.mp4              # Sample video
│
└── __pycache__/           # Python cache files
```

---

## ⚙️ Installation

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Download YOLOv8 Model (if not included)

```bash
pip install ultralytics
```

---

## ▶️ How to Run the Project

Run the main file:

```bash
python main.py
```

You will see the following menu:

```
Select Input Type
1. Image
2. Video
3. Webcam
```

### 📷 Image Detection

Choose option **1** and provide the image path.

Example:

```
Enter image path: image.jpg
```

The system will display:

* Detected objects
* Object counting for each detected class
* Bounding boxes, confidence score and class labels displayed on detected objects

---

### 🎥 Video Detection

Choose option **2** and provide the video path.

Example:

```
Enter video path: video.mp4
```

Features in video mode:

* Object detection in each frame
* Object counting for each detected class
* Bounding boxes, confidence score and class labels displayed on detected objects
* Progress bar
* Mouse-click video seeking
* Pause and resume video playback (Using spacebar keyboard button)
* Press **f** button forward 5 seconds video
* Press **b** button backward 5 seconds video
* Press **q** Quit video

---

### 📹 Webcam Detection

Choose option **3**.

The webcam will start and perform **real-time object detection**.

* Object counting for each detected class
* Bounding boxes, confidence score and class labels displayed on detected objects
* Press **q** to exit.

---

