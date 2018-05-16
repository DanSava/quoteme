from PIL import Image

image_path = 'icons.png'

icons = Image.open(image_path)

nr_lines = 6
nr_columns = 5

w, h = icons.size

thumb_width = w/nr_columns
thumb_height = h/nr_lines

count = 27
for line in range(nr_lines):
    for col in range(nr_columns):
        count += 1
        box = (col * thumb_width, line * thumb_height, (col+1) * thumb_width,  (line + 1) * thumb_height)
        height_offset = 0
        if line == 0:
            box = (col * thumb_width, line * (thumb_height + height_offset), (col+1) * thumb_width,  (line + 1) * thumb_height + height_offset)
        elif line == 1:
            box = (col * thumb_width, line * (thumb_height + height_offset), (col+1) * thumb_width,  (line + 1) * thumb_height + height_offset)

        cropped_image = icons.crop(box)
        cropped_image.save('img/%d.jpg' % count)
