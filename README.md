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
* **Video progress bar**
* **Mouse-click video seeking**
* Pause and resume video playback
* Bounding boxes and class labels displayed on detected objects

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

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/object-detection-yolov8.git
cd object-detection-yolov8
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download YOLOv8 Model (if not included)

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
* Bounding boxes
* Object counts

---

### 🎥 Video Detection

Choose option **2** and provide the video path.

Example:

```
Enter video path: video.mp4
```

Features in video mode:

* Object detection in each frame
* Object counter
* Progress bar
* Clickable video seeking

---

### 📹 Webcam Detection

Choose option **3**.

The webcam will start and perform **real-time object detection**.

Press **Q** to exit.

---

## 📊 Object Counting

The system automatically counts the number of objects detected in each frame.

Example display:

```
person : 3
car : 1
dog : 2
```

---

## 📌 Requirements

The required Python libraries are listed in **requirements.txt**

```
ultralytics
opencv-python
numpy
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* Add **GUI interface**
* Add **object tracking**
* Export detection results to **CSV**
* Support **custom trained YOLO models**
* Improve **video playback controls**

---

## 👨‍💻 Author

**Pranay Katekhaye**

B.Tech IT Student
Machine Learning & Computer Vision Enthusiast

---

## 📜 License

This project is developed for **educational and research purposes**.
