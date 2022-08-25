# Tensorflow/TFserving for [Keras-RetinaNet for Open Images Challenge 2018](https://github.com/ZFTurbo/Keras-RetinaNet-for-Open-Images-Challenge-2018)
This repository is contain convert method and serving solution for RetinaNet which trained on Open Images Object Detection Dataset
## To convert model from h5 to pd
- Select and download an pretrain model from [Keras-RetinaNet Pretrained Models List](https://github.com/ZFTurbo/Keras-RetinaNet-for-Open-Images-Challenge-2018/releases)
- Place it inside ```convert_h5_to_pd/model_input``` 
- Build docker ```sh builddocker.sh``` to create enviroment for converting task
- Run ```sh run.sh``` from inside ```convert_h5_to_pd``` to get the converted model in ```model_output```
- Move converted model inside ```models``` folder ( Example: it will have structure like this)
```shell
models
└── rentinanet-serving
    └── 1
        ├── saved_model.pb
        └── variables
            ├── variables.data-00000-of-00001
            └── variables.index
```
### When pretrained model has already included in the models folder
### 🚀  Step to run:
### Run build docker:
```shell
sh builddocker.sh
```
### Run docker:
```shell
sh run.sh
```
### Run server gradio:
```python
python server.py
```