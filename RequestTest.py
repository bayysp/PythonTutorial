import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://cdn.pixabay.com/photo/2016/04/20/21/17/png-1342113__340.png")
print("Status Code : ", r.status_code)

image = Image.open(BytesIO(r.content))
print(image.size, image.format, image.mode)
path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image")