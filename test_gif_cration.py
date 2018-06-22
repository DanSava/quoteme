import imageio

images_for_gif_paths = ["img/%d.jpg" % (i + 1) for i in range(5)]

with imageio.get_writer('movie.gif', mode='I') as writer:
    for filename in images_for_gif_paths:
        image = imageio.imread(filename)
        writer.append_data(image)