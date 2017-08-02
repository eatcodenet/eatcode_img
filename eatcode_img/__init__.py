class Image:
    """ Simple Image with basic attributes """

    def __init__(self, name, height, width, size_bytes, image_format):
        self.name = name
        self.height = height
        self.width = width
        self.size_bytes = size_bytes
        self.format = image_format
        self.orientation = "portrait" if height > width else "landscape"

    def __str__(self):
        return "Image({}, {}x{}, {}, {}, {})".format(self.name,
                                                     self.height,
                                                     self.width,
                                                     self.size_bytes,
                                                     self.format,
                                                     self.orientation)
