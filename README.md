# Face Mask Detection Using PyTorch

A deep learning project for real-time face mask detection using PyTorch, Transfer Learning (MobileNetV2), and OpenCV. This repository contains all code and instructions needed to train a model and perform inference on images or live webcam video streams.

---

## ✨ Features

- Mask vs. No-Mask image classification using CNN and transfer learning
- Real-time detection/inference with OpenCV
- Dataset augmentation for robust model performance
- Simple folder structure and modular code
- Detailed instructions for setup and reproducibility

---

## 📁 Project Structure
ace_mask_detection_using_PyTorch/
│
├── Train_Model/
│ ├── data/
│ │ ├── train/
│ │ │ ├── mask/
│ │ │ └── no_mask/
│ │ └── test/
│ │ ├── mask/
│ │ └── no_mask/
│ └── Train_Model.py
│
├── Use_Model/
│ └── faceDetect.py
│
├── Face_Extractor/
│ └── app.py
│
└── README.md

