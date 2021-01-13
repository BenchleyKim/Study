import io
import json
import os
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
imagenet_class_index = json.load(open('./imagenet_class_index.json'))
model = models.densenet121(pretrained=True)
model.eval()


def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]

@app.route('/predict', methods= ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        file.save("./static/img/image.jpg")
        # return jsonify({'class_id': class_id, 'class_name': class_name})
        return render_template('upload.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method =='POST' :
        f = request.files['file']
        f.save("./images/"+secure_filename(f.filename))
        return 'uploads 디렉토리 > 파일 업로드 성공'
    else :
        return "잘못된 접근입니다."

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()