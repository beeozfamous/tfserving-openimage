import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="0"

from keras_retinanet import models
from keras import backend as K
import tensorflow as tf


# Change model type and backbone here
pretrained_model_path = 'model_input/retinanet_resnet101_500_classes_0.4986_converted.h5'
backbone = 'resnet50'

export_dir_path = 'model_output/rentinanet-serving/1'

convert_model = models.load_model(pretrained_model_path, backbone_name=backbone)

# Convert and save
with tf.keras.backend.get_session() as sess:
    tf.saved_model.simple_save(
        sess,
        export_dir_path,
        inputs={'input_image': convert_model.input},
        outputs={'out0': convert_model.output[0], 'out1' : convert_model.output[1],'out2': convert_model.output[2]})