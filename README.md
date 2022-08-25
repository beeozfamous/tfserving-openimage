# Tensorflow/TFserving for [Keras-RetinaNet for Open Images Challenge 2018](https://github.com/ZFTurbo/Keras-RetinaNet-for-Open-Images-Challenge-2018)

## It currently using the inference pretrained RetinaNet model base on ResNet101 for all 500 classes of OpenImageDataset for Object Detection

| Backbone | Image Size (px) | Model (training) | Model (inference) | Small validation mAP | Full validation mAP |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ResNet101 | 768 - 1024	 | 752 MB	 | 251 MB | 0.4986	 | 0.4520
 |

## The pretrained model has already included in the models folder, which already convert from Keras(.h5) to Tensorflow(.pd)
## Step to run:
### 🚀 Run build docker:
```shell
sh builddocker.sh
```
### 🚀 Run docker:
```shell
sh run.sh
```
### 🚀 Run server gradio:
```python
python server.py
```