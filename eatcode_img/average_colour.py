from PIL import Image
import os


def average(src_img_file):
    """ Gets the simple average colour for a given images file """
    colour_tuple = [None, None, None]
    try:
        img = Image.open(src_img_file)
        # Get data for one channel at a time
        for channel in range(3):
            pixels = img.getdata(band=channel)
            values = []
            for pixel in pixels:
                values.append(pixel)
            colour_tuple[channel] = sum(values) / len(values)

        avg_colour = tuple(map(int, colour_tuple))
        _create_avg_file(avg_colour, img, src_img_file)
    except IOError:
        print("Error opening file", src_img_file)


def _create_avg_file(avg_colour, img, src_img_file):
    img_out = Image.new(img.mode, img.size)
    img_out.paste(avg_colour, (0, 0, img.size[0], img.size[1]))
    (file, ext) = os.path.splitext(src_img_file)
    img_out.save(file + ".avg" + ext)


if __name__ == '__main__':
    average("/home/ayub/Downloads/mona.jpg")  # WIP
