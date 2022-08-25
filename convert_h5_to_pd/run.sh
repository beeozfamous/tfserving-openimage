docker run --rm -it --name mar -v $(pwd)/model_output:/model_output -v \
$(pwd)/model_input:/model_input python convert.py