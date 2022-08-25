docker run --rm -it --name mar -v $(pwd)/model_output:/model_output -v \
$(pwd)/model_input:/model_input tfserving:build_retina python convert.py