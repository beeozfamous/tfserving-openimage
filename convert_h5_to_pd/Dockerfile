FROM tensorflow/tensorflow:1.15.3-gpu-py3-jupyter

RUN apt-get update
RUN apt-get install wget
RUN apt-get update
RUN apt-get install git
RUN apt-get install tensorflow-model-server


RUN wget 'http://storage.googleapis.com/tensorflow-serving-apt/pool/tensorflow-model-server-1.15.0/t/tensorflow-model-server/tensorflow-model-server_1.15.0_all.deb'
RUN dpkg -i tensorflow-model-server_1.15.0_all.deb
RUN pip3 install tensorflow-serving-api==1.15
RUN pip3 install -r requirements.txt
COPY . .

#ENTRYPOINT ['python3','convert.py']

