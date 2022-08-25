docker run --rm --runtime=nvidia -e TF_CPP_MIN_VLOG_LEVEL=1 -e NVIDIA_VISIBLE_DEVICES=0 --gpus device=0 -p 8501:8501 \
--mount type=bind,\
source=/home/dev-fti/khang/nguyen/pixguru_object_detection/models/rentinanet-serving/1,\
target=/home/dev-fti/khang/nguyen/pixguru_object_detection/models/rentinanet-serving/1 \
  -e MODEL_NAME=rentinanet-serving -t tfserving:retina &
