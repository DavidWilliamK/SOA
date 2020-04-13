from flask import Flask, jsonify, request, g, json, flash, redirect, url_for
from flask_cors import CORS
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import time
import requests
import os

# Config
DEBUG = True
UPLOAD_FOLDER = 'D:/David/8th Semester/1st Period/SOA/Lecture/Assignment/Project/backend/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/soa'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mongo = PyMongo(app)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.before_request
def before_request():
    g.start = time.time()

@app.after_request
def after_request(response):
    diff = time.time() - g.start
    if ((response.response) and
        (200 <= response.status_code < 300) and
        (response.content_type.startswith('text/html'))):
        response.set_data(response.get_data().replace(
            b'__EXECUTION_TIME__', bytes(str(diff), 'utf-8')))
    print(f'{diff} seconds')
    return response

@app.route('/')
def hello_world():
    return 'Hello World!'

# Sanity check
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/save', methods=['POST'])
def create():
    images = []
    for idx in range (int(request.form['count'])):
        if 'files['+str(idx)+']' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['files['+str(idx)+']']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            mongo.db.images.insert({'filename': file.filename, 'path': UPLOAD_FOLDER+file.filename})
            images.append(UPLOAD_FOLDER+file.filename)
    print(json.dumps({'instances': images}))
    r = requests.post(
        'http://127.0.0.1:5000/detect',
        data=json.dumps({'instances': images})
    )
    for image in r:
        for detected_object in image:
            x, y, w, h = cv2.boundingRect(detect_image)
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
    return r


@app.route('/detect', methods=['POST'])
def detect_image():
    url = 'http://52.79.114.190:8501/v1/models/mobilenetssd:predict'
    img_arr = []
    img_size = []
    if request.method == 'POST':
        instances = []
        post_data = request.get_json()
        print(post_data)
        for data in post_data.get('instances'):
            image = cv2.imread(data)
            image = cv2.resize(image, (720, 720), interpolation=cv2.INTER_AREA)
            instances.append(image.tolist())
            img_size.append(image.shape)
        img_arr = np.array(instances).tolist()
        headers = {"content-type": "application/json"}
        r = requests.post(
            url,
            data=json.dumps({'instances': img_arr}),
            headers=headers,
            verify=False,
            timeout=30
        )
        print(r.text)
        detection = json.loads(r.content.decode('utf8'))
        response = []
        for prediction in detection['predictions']:
            idx = []
            bounding_boxes = []
            print(prediction)
            for score in prediction['scores']:
                if score > 0.5:
                    idx.append(prediction['scores'].index(score))
            for box in idx:
                bounding_boxes.append(prediction['boxes'][box])
            response.append(bounding_boxes)
        for box in bounding_boxes:
            print(f'Box: {box} on index {bounding_boxes.index(box)}')
            for point in box:
                if box.index(point) % 2 == 0:
                    new_point = point*img_size[bounding_boxes.index(box)][0]
                else:
                    new_point = point*img_size[bounding_boxes.index(box)][1]
                box[box.index(point)] = new_point
            print(f'New box: {box}')
        print(f'Will respond with: {response}')
        return json.dumps(response)

if __name__ == '__main__':
    app.run()
