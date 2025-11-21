# Sensor-Data-Fusion
Collection of sensor fusion and computer vision projects: IMU accelerometer–gyroscope processing, complementary filters, Kalman Filters, face detection (Viola–Jones), YOLO object detection, camera calibration, data visualization and real-time tracking experiments.
A complete Python collection of algorithms and tools used in Sensor Networks & Sensor Fusion — including IMU processing, accelerometer/gyroscope fusion, complementary filtering, Kalman Filters, computer vision (Viola–Jones, YOLO), camera calibration, and real-time visualization utilities.

This repository is designed for students, researchers, and engineers working with robotics, drones, autonomous systems, or embedded platforms.

🚀 Features
🔵 IMU Processing & Fusion

Accelerometer-based orientation estimation

Gyroscope integration (raw angle estimation)

Complementary Filter for stable roll/pitch estimation

Real-time fusion of accelerometer + gyro

Drift reduction & noise-robust filtering

Playback of recorded IMU datasets

🟢 Kalman Filters

Linear Kalman Filter (KF)

Constant Velocity (CV) model

Constant Acceleration (CA) model

Extended Kalman Filter (EKF)

Unscented Kalman Filter (UKF)

🔶 Computer Vision

Camera Calibration utilities

Viola–Jones face detection

YOLO-based object detection and experiments

🔧 Utility Tools

Data reader for streamed or recorded sensor values

Real-time plotting using DearPyGui

File I/O helpers

Mathematical helper functions
...
🗂 Project Structure
sensor-data-fusion/
│
├── src/
│   ├── fusion/                # IMU fusion algorithms
│   ├── kalman/                # Kalman filter modules
│   ├── vision/                # Vision tools (camera, detection)
│   └── utils/                 # Shared utilities (plotting, file IO)
│
├── data/                      # IMU recordings, calibration files
│   └── imudata.txt
│
├── examples/                  # Ready-to-run demos
├── notebooks/                 # Experiments + exploration
└── README.md
...
📊 Real-Time IMU Visualization

The repository includes a real-time visualization dashboard built with DearPyGui:

3-axis accelerometer

3-axis gyroscope

Accelerometer-derived angles

Gyroscope-integrated angles

Complementary filter orientation

Works with both:

Live sensor data

Recorded datasets (imudata.txt)

🧪 Example: Complementary Filter Output

This repository contains clean and modular implementations of:

accel_to_angle() → roll/pitch from accelerometer

GyroIntegrator → integrating gyro rates

ComplementaryFilter → fused orientation estimation

Fusion equation:

θ_fused = (1 - k) * (θ_gyro + ω * dt) + k * (θ_accel)


Where:

gyro = stable short-term, drifts long-term

accelerometer = noisy short-term, stable long-term

typical k ≈ 0.02–0.05

📁 Dataset Included
imudata.txt

A 30-second IMU recording with:

timestamp

accelerometer (ax, ay, az)

gyroscope (p, q, r)

Used for evaluating:

accelerometer-only orientation

gyro-only orientation

fused complementary filter output

🛠 Requirements
numpy
matplotlib
dearpygui
scipy


(Additional libraries such as OpenCV or Ultralytics may be required for YOLO/CV modules.)

🎯 Goals of This Repository

This project grows as part of coursework and experimentation in Sensor Networks & Data Fusion.
It aims to provide:

A complete portfolio project

A practical template for sensor fusion pipelines

A clean implementation of classical filtering techniques

A playground for robotics & embedded system exploration

👤 Author

Shumit Roy
Technische Hochschule Ingolstadt
Sensor Networks & Sensor Fusion
