import json
from util import build_image
import imageio
with open('../factsdb/facts.json') as f:
    data = json.load(f)


font_path = "../fonts/ChalkFont-Regular.ttf"
thumb_size = 50
img_width = 1200
img_height = 800
text_wrap_width = 40
font_size = 38


for x in range(len(data['facts'])):
    print("Bulding gif no:", x)
    images_for_gif_paths = []
    for gif_img_index in range(3):
        image = build_image(img_width, img_height, data['facts'][x], text_wrap_width, font_path, font_size, thumb_size)
        # Saving the image to disk
        path = '../output/gifs/temp/%d.jpg' % gif_img_index
        image.save(path)
        images_for_gif_paths.append(path)

    with imageio.get_writer('../output/gifs/%d.gif' % x, mode='I') as writer:
        for filename in images_for_gif_paths:
            image = imageio.imread(filename)
            writer.append_data(image)
