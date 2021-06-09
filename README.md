# RangRang - Machine Learning

<p align="center">
  <img src="assets/logo.png" alt="logo" width="300px" height="300px" />
</p>

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
[![TensorFlow 2.3](https://img.shields.io/badge/TensorFlow-2.3-FF6F00?logo=tensorflow)](https://github.com/tensorflow/tensorflow/releases/tag/v2.3.0)

Bagian pembelajaran mesin dari project capstone bangkit tim `uwuwu` -> `RangRang`

## To Do

1. Mencari data untuk `object detection` & `color detection`
2. Membuat model menggunakan `tensorflow`<br>
   Model yang harus di buat:
   1. object detection model
   2. color detection model

## Update on Object Detection Model

1. Karena harus ada custom trainingnya maka model akan di fine tune dengan dataset baru menggunakan tensorflow object detection library

## Update on Color Detection Model

1. Sama seperti Object Detection
   
## Sumber Bacaan

1. [Object Detection API with TensorFlow 2](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md)
2. [Training Custom Object Detector](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)
3. Transfer Learning Object detection model - [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
4. [Running TF2 Detection API Models on mobile](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tf2.md)
5. [Real-time Object Detection using SSD MobileNet V2 on Video Streams](https://heartbeat.fritz.ai/real-time-object-detection-using-ssd-mobilenet-v2-on-video-streams-3bfc1577399c)
6. [color detection](https://towardsdatascience.com/image-color-identification-with-machine-learning-and-image-processing-using-python-f3dd0606bdca)
7. [color detection 2](https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71)


## Scripts

### 1. Image Downloader

Download image dari google image dengan query yang bisa di atur di `scripts\query.json` dengan cara

1. Install `google-image-downloader` library
   ```
   git clone https://github.com/Joeclinton1/google-images-download.git
   cd google-images-download 
   python setup.py install
   ```
2. Run `image_downloader.py`
   ```
   python workspace/training_demo/scripts/image_downloader.py
   ```

Setelah itu hasil download akan terdapat pada folder `downloads`

**Note**

Untuk jumlah `limit > 100` download `chromedriver` [di sini](https://sites.google.com/a/chromium.org/chromedriver/downloads) lalu extract pada suatu folder. Lalu run `image_downloader.py` dengan argumen `-c`. Contoh

```
python scripts/image_downloader.py -c C:/tools/chromedriver/chromedriver.exe
```