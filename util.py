from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
from random import shuffle


def construct_image_frame(width, height, thumbs_path_list, thumb_size, clip_rect=(150, 150, 1000, 200)):
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


def build_image(img_width, img_height, text, text_wrap_width, font_path, font_size, thumb_size, index_image):
    thumb_paths = ["img/%d.jpg" % (x + 1) for x in range(57)]
    text_wrapped = textwrap.wrap(text, width=text_wrap_width)
    img = construct_image_frame(width=img_width, height=img_height, thumbs_path_list=thumb_paths, thumb_size=thumb_size,
                                clip_rect=(150, 150, 1000, 200 + (thumb_size * len(text_wrapped))))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    for line_nr, text_line in enumerate(text_wrapped):
        draw.text((200 + 10, 200 + line_nr * (font_size + 10)),
                  text_line,
                  (0, 0, 0),
                  font=font)

    # Adding the little bits log to the image
    img = add_logo_to_image(img, "logo/logo.png", thumb_size)

    # Saving the image to disk
    img.save('output/lbs_%d.jpg' % index_image)
