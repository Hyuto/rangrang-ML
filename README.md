# RangRang - Machine Learning

<p align="center">
  <img src="assets/logo.png" alt="logo" width="300px" height="300px" />
</p>

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
[![TensorFlow 2.3](https://img.shields.io/badge/TensorFlow-2.3-FF6F00?logo=tensorflow)](https://github.com/tensorflow/tensorflow/releases/tag/v2.3.0)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Hyuto/rangrang-ML/blob/master/notebook/RangRang_ML.ipynb)


Machine Learning side of `RangRang`

## To Do's

1. Create data for `object detection` and `color detection` level :heavy_check_mark:
2. Labelling images :heavy_check_mark:
3. Create the model using `tensorflow object detection API` :heavy_check_mark:

## Update on Object Detection Model

Fine tune `ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8` model with data on the `workspace/object_detection/images`

## Update on Color Detection Model

Fine tune `ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8` model with data on the `workspace/color_detection/images`

## Dataset

* [Dwiki Kusuma : living room object data](https://www.kaggle.com/dwikikusuma/living-room-object-data) on Kaggle

## Scripts

```
scripts
├── add_metadata.py
├── check_image.py
├── convert_tflite.py
├── image_downloader.py
├── label_processing.py
├── preprocessing
│   ├── generate_tfrecord.py
│   ├── partition_dataset.py
│   └── renamer.py
└── query.json
```

## References

1. [Object Detection API with TensorFlow 2](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md)
2. [Training Custom Object Detector](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)
3. Transfer Learning Object detection model - [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
4. [Running TF2 Detection API Models on mobile](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tf2.md)
5. [Real-time Object Detection using SSD MobileNet V2 on Video Streams](https://heartbeat.fritz.ai/real-time-object-detection-using-ssd-mobilenet-v2-on-video-streams-3bfc1577399c)
6. [Color Detection](https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71)

## Navigation 

|      | Repository |
| :--- | :--------: |
| Android | [grrrracia/RangRang-MobileApp](https://github.com/grrrracia/RangRang-MobileApp) |
| Cloud Computing | [Hyuto/rangrang-server](https://github.com/Hyuto/rangrang-server) |
| Machine Learning | [Hyuto/rangrang-ML](https://github.com/Hyuto/rangrang-ML) |