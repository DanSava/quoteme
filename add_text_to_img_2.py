from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from util import construct_image_frame, add_logo_to_image
import textwrap


def build_image(img_width, img_height, text, text_wrap_width, font_path,font_size, thumb_size, index_image):
    thumb_paths = ["img/%d.jpg" % (x+1) for x in range(57)]
    text_wrapped = textwrap.wrap(text, width=text_wrap_width)
    img = construct_image_frame(width=img_width, height=img_height, thumbs_path_list=thumb_paths, thumb_size=thumb_size, clip_rect=(150, 150, 1000, 200 + (thumb_size * len(text_wrapped))))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    for line_nr, text_line in enumerate(text_wrapped):
        print(len(text_line), text_line)
        draw.text((200+10, 200 + line_nr * (font_size + 10)),
                  text_line,
                  (0, 0, 0),
                  font=font)

    # Adding the little bits log to the image
    img = add_logo_to_image(img, "logo/logo.png", thumb_size)

    # Saving the image to disk
    img.save('output/lbs_%d.jpg' % index_image)
