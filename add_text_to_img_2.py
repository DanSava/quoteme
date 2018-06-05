from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from util import construct_image
import textwrap

thumb_paths = ["img/%d.jpg" % (x+1) for x in range(57)]
text = "For the first time in human history, gene-editing has been performed to fix a mutation for an inherited disease in embryos. Using a powerful tool called Crispr-Cas9, scientists successfully altered the DNA in defective embryos so they were no longer programmed to develop congenital heart failure."
text_wrapped = textwrap.wrap(text, width=40)
print(len(text_wrapped))
thumb_size = 50
img_width = 1200
img_height = 800

img = construct_image(width=img_width, height=img_height, thumbs_path_list=thumb_paths, thumb_size=thumb_size, clip_rect=(150, 150, 1000, 200 + (thumb_size * len(text_wrapped))))
draw = ImageDraw.Draw(img)
width, height = img.size
font_size = 38
font_path = "fonts/ChalkFont-Regular.ttf"
font = ImageFont.truetype(font_path, font_size)
for line_nr, text_line in enumerate(text_wrapped):
    print(len(text_line), text_line)
    draw.text((200+10, 200 + line_nr * (font_size + 10)),
              text_line,
              (0, 0, 0),
              font=font)

img.save('little_bits_sci1.jpg')
