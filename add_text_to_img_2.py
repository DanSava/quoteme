from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from utils import construct_image
import textwrap

thumb_paths = ["img/%d.jpg" % (x+1) for x in range(57)]

img = construct_image(thumbs_path_list=thumb_paths, clip_rect=(150, 200, 1000, 450))
draw = ImageDraw.Draw(img)
width, height = img.size
font_size = 40
font_path = "fonts/ChalkFont-Regular.ttf"
text = "It takes 8 minutes 17 seconds for light to travel from the Sun’s surface to the Earth"
text_wrapped = textwrap.wrap(text, width=42)
font = ImageFont.truetype(font_path, font_size)
for line_nr, text_line in enumerate(text_wrapped):
    draw.text((width * 0.175, 300 + line_nr * (font_size + 10)),
              text_line,
              (0, 0, 0),
              font=font)

img.save('little_bits_sci1.jpg')


# quote_font_size = 90
# author_font_size = 40
# text_width = 25
#
# ## Draw quote text ##
# quote_text_wrapped = textwrap.wrap(data[i]["Quote"], width=text_width)
# while len(quote_text_wrapped) > 4:
#     quote_font_size -= 10
#     text_width += 5
#     quote_text_wrapped = textwrap.wrap(data[i]["Quote"], width=text_width)
# font = ImageFont.truetype("Pacifico-Regular.ttf", quote_font_size)
