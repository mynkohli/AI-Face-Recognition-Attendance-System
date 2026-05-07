# AI Face Recognition Attendance System

An AI-powered attendance management system built using Python, OpenCV, and face recognition technology for real-time facial detection and automated attendance tracking.

---

## Features

- Real-time face detection
- Face recognition using webcam
- Automatic attendance marking
- CSV-based attendance storage
- Duplicate attendance prevention
- Live webcam feed with face labels

---

## Tech Stack

- Python
- OpenCV
- face_recognition
- NumPy
- Pandas

---

## Project Structure

```bash
Face-Recognition-Attendance-System
│
├── images
│   ├── mayank.jpg
│   └── chungli.jpg
│
├── main.py
├── Attendance.csv
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/mynkohli/AI-Face-Recognition-Attendance-System.git
```

### Install Dependencies

```bash
pip install opencv-python
pip install face_recognition
pip install numpy
pip install pandas
```

---

## Run Project

```bash
python main.py
```

---

## Output

- Webcam opens automatically
- Detects registered faces
- Displays recognized name
- Stores attendance with date and time

---

## Sample Attendance Record

```csv
Name,Time,Date
MAYANK,12:45:20,07-05-2026
```

---

## Future Improvements

- GUI Dashboard
- Database Integration
- Flask Web App
- Cloud Deployment
- Mobile Camera Support
- Liveness Detection

---

## Author

Mayank Kohli
