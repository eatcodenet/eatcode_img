from PIL import Image


def average_colour2(img_file):
    """ Gets the simple average colour for a given images file """
    colour_tuple = [None, None, None]
    try:
        image = Image.open(img_file)
        for channel in range(3):
            # Get data for one channel at a time
            pixels = image.getdata(band=channel)
            values = []
            for pixel in pixels:
                values.append(pixel)
            colour_tuple[channel] = sum(values) / len(values)

        avg = tuple(map(int, colour_tuple))
        img_out = Image.new(image.mode, image.size)
        img_out.paste(avg, (0, 0, image.size[0], image.size[1]))
        img_out.save("/home/ayub/Downloads/avg.jpg")
    except IOError:
        print("Error opening file", img_file)


if __name__ == '__main__':
    average_colour2("/home/ayub/Downloads/mona.jpg")
