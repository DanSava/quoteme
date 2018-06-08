import json
from util import build_image

from pprint import pprint

with open('factsdb/facts.json') as f:
    data = json.load(f)
print(len(data['facts']))

text = data['facts'][1]
font_path = "fonts/ChalkFont-Regular.ttf"
thumb_size = 50
img_width = 1200
img_height = 800
text_wrap_width = 40
font_size = 38

for x in range(3):
    build_image(img_width, img_height, data['facts'][x], text_wrap_width, font_path, font_size, thumb_size, x)

