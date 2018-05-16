from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json as json
import textwrap

data = []
with open('data.json') as data_file:
    data = json.load(data_file)

for i in range(20):
    img = Image.open("image.jpg")
    draw = ImageDraw.Draw(img)
    width, height = img.size
    quote_font_size = 90
    author_font_size = 40
    text_width = 25

    ## Draw quote text ##
    quote_text_wrapped = textwrap.wrap(data[i]["Quote"], width=text_width)
    while len(quote_text_wrapped) > 4:
        quote_font_size -= 10
        text_width += 5
        quote_text_wrapped = textwrap.wrap(data[i]["Quote"], width=text_width)
    font = ImageFont.truetype("Pacifico-Regular.ttf", quote_font_size)
    for line_nr, text_line in enumerate(quote_text_wrapped):
        draw.text((width * 0.05, height / 3 + line_nr * (quote_font_size + 10)),
                  text_line,
                  (255, 255, 255),
                  font=font)

    ## Draw author ##
    author_text_wrapped = textwrap.wrap(data[i]["Author"], width=20)
    font_author = ImageFont.truetype("chalk_font.ttf", author_font_size)
    for line_nr, text_line in enumerate(author_text_wrapped):
        draw.text((width * 0.75, height * 0.15 + line_nr * (author_font_size + 5)),
                  text_line,
                  (255, 255, 255),
                  font=font_author)


    img.save('test/test-out_%d.jpg' % i)
