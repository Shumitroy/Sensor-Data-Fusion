A comprehensive collection of sensor fusion and computer vision projects implemented in Python.
This repository includes IMU accelerometer–gyroscope processing, complementary filtering, Kalman Filters, Viola–Jones face detection, YOLO object detection, camera calibration, data visualization, and real-time tracking tools.

Designed for students, researchers, and engineers working on robotics, drones, autonomous systems, embedded devices, or anyone learning Sensor Networks & Data Fusion.
🚀 Features
🔵 IMU Processing & Fusion

Accelerometer-based orientation estimation

Gyroscope integration (raw angle computation)

Complementary Filter for stable roll/pitch estimation

Real-time accelerometer + gyro fusion

Noise-resistant filtering & drift reduction

Playback of recorded IMU datasets

🟢 Kalman Filters

Linear Kalman Filter (KF)

Constant Velocity (CV) model

Constant Acceleration (CA) model

Extended Kalman Filter (EKF)

Unscented Kalman Filter (UKF)

🔶 Computer Vision

Camera calibration utilities

Viola–Jones face detection (Haar cascades)

YOLO-based deep-learning object detection

🔧 Utility Tools

Data reader for streamed or recorded data

Real-time visualization using DearPyGui

File I/O helpers

Mathematical helper functions
sensor-data-fusion/
│
├── src/
│   ├── fusion/                # IMU fusion algorithms
│   ├── kalman/                # Kalman filter models
│   ├── vision/                # Camera calibration & detection tools
│   └── utils/                 # Plotting, math & file utilities
│
├── data/                      # IMU recordings, calibration files
│   └── imudata.txt
│
├── examples/                  # Ready-to-run demo scripts
├── notebooks/                 # Jupyter experiments
└── README.md
📊 Real-Time IMU Visualization

Includes a real-time visualization dashboard using DearPyGui, showing:

3-axis accelerometer

3-axis gyroscope

Accelerometer-derived roll/pitch

Gyroscope-integrated orientation

Complementary filter fused output

Works with:

Live streaming IMU data

Pre-recorded dataset (imudata.txt)

🧪 Complementary Filter Example

This project includes clear implementations of:

accel_to_angle() → roll/pitch from accelerometer

GyroIntegrator → integrate angular velocity

ComplementaryFilter → fused orientation estimate

Fusion Equation:

θ_fused = (1 - k) * (θ_gyro + ω * dt) + k * (θ_accel)


Where:

Gyroscope = stable short-term, drifts long-term

Accelerometer = noisy short-term, stable long-term

Typical k ≈ 0.02–0.05
📁 Dataset Included
imudata.txt

A 30-second IMU recording containing:

timestamp

accelerometer (ax, ay, az)

gyroscope (p, q, r)

Useful for evaluating:

Accelerometer-only orientation

Gyro-only orientation

Complementary filter fusion

🛠 Requirements
numpy
matplotlib
dearpygui
scipy


Additional optional packages (for CV/YOLO):

opencv-python
ultralytics
torch

🎯 Goal of This Repository

This project is part of academic coursework and self-driven experimentation in Sensor Networks & Data Fusion.
It aims to provide:

A complete portfolio project

A practical template for sensor fusion pipelines

Clean implementations of core filtering techniques

A playground for robotics and embedded system exploration

👤 Author

Shumit Roy
Technische Hochschule Ingolstadt
Sensor Networks & Sensor Fusion
