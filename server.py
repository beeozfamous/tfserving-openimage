import json
import requests
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf
from src.utils import resize_image,preprocess_image, read_image_bgr_fast
from src.label import ALL_LABELS,COLOR_LIST
import gradio as gr

image_path = 'bike.jpeg'
image = np.array(Image.open(image_path))


def show_preds(input_image):
    # Read image

    image = np.array(input_image)
    image_copy = image.copy()
    image = read_image_bgr_fast(image)

    BACKBONE = 'resnet152'
    # Pre-processing
    image = preprocess_image(image)
    if BACKBONE == 'resnet152':
        image, scale = resize_image(image, min_side=600, max_side=800)
    elif BACKBONE == 'resnet101':
        image, scale = resize_image(image, min_side=768, max_side=1024)

    copy_image = image.copy()

    # Convert the Tensor to a batch of Tensors and then to a list
    image_tensor = tf.expand_dims(image, 0)
    image_tensor = image_tensor.numpy().tolist()

    data = json.dumps({
        "instances": image_tensor
    })
    headers = {"content-type": "application/json"}

    # server's properties
    port = 8501
    server_name = 'rentinanet-serving'
    server_url = 'http://0.0.0.0:{}/v1/model_input/{}:predict'.format(port, server_name)

    # Predict
    response = requests.post(server_url, data=data, headers=headers)

    # Draw all label
    copy_image = resize_image(image_copy[:, :, ::-1], min_side=600, max_side=800)[0]
    pointx = []
    for i in range(500):
        point = response.json()['predictions'][0]['out0'][i]
        print(point)
        prob = response.json()['predictions'][0]['out1'][i]
        label_number = response.json()['predictions'][0]['out2'][i]

        label_name = ALL_LABELS[label_number]
        color_code = COLOR_LIST[label_number]
        if prob > 0.5:
            copy_image = cv2.rectangle(copy_image, (int(point[0]), int(point[1])), (int(point[2]), int(point[3])),
                                       color_code, 2)
            cv2.putText(copy_image, "{}-{} [{}]".format(label_number, label_name, round(prob, 3)),
                        (int(point[0]), int(point[1]) + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color_code, 1)
        print("{} - {} - {}".format(label_number, label_name, prob))

        if i == 10:
            break

    return copy_image[:, :, ::-1]
if __name__ == "__main__":

    gr_interface = gr.Interface(
        fn=show_preds,
        inputs=["image"],
        outputs=[gr.outputs.Image(type="pil", label="RetinaNet Inference")],
        title="Fridge Object Detector",
        description="A VFNet model that detects common objects found in fridge. Upload an image or click an example image below to use.",
    #     examples=examples,
    )
    gr_interface.launch(inline=False, share=True, debug=True)