import pickle

from flask import Flask
from flask import request
from flask import jsonify
import numpy as np 
import urllib.request
import ssl 

ssl._create_default_https_context = ssl._create_unverified_context


model_file = './models/model_regression.pickle'

def get_optimal_quality(url):
    try:
        d = urllib.request.urlopen(url)
        file_size_bits = int(d.info()['Content-Length']) * 8 
        try:
            h, w = d.info()['Fastly-Io-Info'].split(' ')[1].split('x')
            h, w = int(h.split('=')[1]), int(w)
            bpp = (file_size_bits)/(h*w)
            if bpp > 4.15:
                return 50

            else:
                x_test = np.array([bpp]).reshape((-1, 1))
                score = round(model.predict(x_test)[0], 4)
                return score
        except AttributeError:
            return "The Image is not registered on Contentstack or Fastly"
    except ValueError:
        return "The image cannot be rendered from the given url"


with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('optimal-image')

@app.route('/predict', methods=['POST'])
def predict():
    img_link = request.get_json()
    quality = get_optimal_quality(img_link['image_path'])
    result = {
        "quality":quality
    }

    return jsonify(result)

@app.route('/')
def health_check():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)