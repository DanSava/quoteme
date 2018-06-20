import json
from util import build_image


with open('../factsdb/facts.json') as f:
    data = json.load(f)


font_path = "../fonts/ChalkFont-Regular.ttf"
thumb_size = 50
img_width = 1200
img_height = 800
text_wrap_width = 40
font_size = 38

for x in range(len(data['facts'])):
    image = build_image(img_width, img_height, data['facts'][x], text_wrap_width, font_path, font_size, thumb_size)
    # Saving the image to disk
    image.save('../output/lbs_%d.jpg' % x)
