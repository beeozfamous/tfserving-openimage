FROM tensorflow/tensorflow:1.15.3-gpu-py3-jupyter

RUN apt-get install -y --no-install-recommends wget
RUN apt-key del 7fa2af80
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb

COPY . .

RUN apt-get update

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get install wget
RUN apt-get update


RUN wget 'http://storage.googleapis.com/tensorflow-serving-apt/pool/tensorflow-model-server-1.15.0/t/tensorflow-model-server/tensorflow-model-server_1.15.0_all.deb'
RUN dpkg -i tensorflow-model-server_1.15.0_all.deb
RUN apt-get install tensorflow-model-server -
RUN pip3 install tensorflow-serving-api==1.15
RUN pip3 install -r requirements.txt

#ENTRYPOINT ['python3','convert.py']

