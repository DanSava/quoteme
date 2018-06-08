from PIL import Image
from random import shuffle


def construct_image(width, height, thumbs_path_list, thumb_size, clip_rect=(150, 150, 1000, 200)):
    result = Image.new("RGB", (width, height), color='white')
    nr_lines = int(height/thumb_size)
    nr_columns = int(width/thumb_size)
    img_index = [x + 1 for x in range(len(thumbs_path_list)-1)]
    shuffle(img_index)
    array_pos = 0
    for line in range(nr_lines):
        for col in range(nr_columns):
            if array_pos >= len(img_index):
                array_pos = 0
            img = Image.open(thumbs_path_list[img_index[array_pos]])
            img.thumbnail((thumb_size, thumb_size), Image.ANTIALIAS)
            x = col * thumb_size
            y = line * thumb_size

            if clip_rect[0] < x < clip_rect[2] and clip_rect[1] < y <= clip_rect[3]:
                pass
            else:
                w, h = img.size
                result.paste(img, (x, y, x + w, y + h))
                array_pos += 1
    return result


def add_logo_to_image(img, logo_path,logo_size):
    img_width, img_height = img.size
    logo = Image.open(logo_path)
    logo.thumbnail((logo_size, logo_size), Image.ANTIALIAS)
    img.paste(logo, (img_width - logo_size, img_height - logo_size, img_width, img_height))
    return img
