import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import urllib.request
import ssl
from PIL import Image
from io import BytesIO
import uvicorn 

ssl._create_default_https_context = ssl._create_unverified_context

model_file = './models/model_regression.pickle'

class ImagePath(BaseModel):
    image_path: str

def get_optimal_quality(url):
    try:
        d = urllib.request.urlopen(url)
        file_size_bits = int(d.info()['Content-Length']) * 8
        try:
            h, w = d.info()['Fastly-Io-Info'].split(' ')[1].split('x')
            h, w = int(h.split('=')[1]), int(w)
            bpp = (file_size_bits) / (h * w)
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
    
def get_optimal_quality_(url):
    try:
        d = urllib.request.urlopen(url)
        image_bytes = d.read()
        image_io = BytesIO(image_bytes)
        pillow_image = Image.open(image_io)
        file_size_bits = image_io.getbuffer().nbytes * 8
        h, w = pillow_image.size
        bpp = (file_size_bits) / (h * w)
        if bpp > 4.15:
            return 50
        else:
            x_test = np.array([bpp]).reshape((-1, 1))
            score = round(model.predict(x_test)[0], 4)
            return score
        # print(image_io.tell())
    except:
        return 0.


with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = FastAPI()

@app.post("/predict")
def predict(image_path: ImagePath):
    quality = get_optimal_quality_(image_path.image_path)
    result = {"quality": quality}
    return result

@app.get("/")
def health_check():
    return "ok"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
