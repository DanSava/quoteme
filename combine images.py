from PIL import Image
from random import randint, shuffle

result = Image.new("RGB", (1200, 800), color='white')
nr_lines = 16
nr_columns = 24
thumb_size = 50

for line in range(nr_lines):
    for col in range(nr_columns):
        if 3 < col < 20 and 3 < line < 12:
            pass
        else:
            image_to_use = randint(1, 57)
            img = Image.open('img/%d.jpg' % image_to_use)
            img.thumbnail((thumb_size, thumb_size), Image.ANTIALIAS)
            x = col * thumb_size
            y = line * thumb_size
            w, h = img.size
            result.paste(img, (x, y, x + w, y + h))

result.save('img/result.jpg')
