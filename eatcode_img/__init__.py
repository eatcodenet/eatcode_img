class Image:
    """ Simple Image with basic attributes """

    def __init__(self, name, height, width, size_bytes, image_format='Unknown'):
        self.name = name
        self.height = height
        self.width = width
        self.size_bytes = size_bytes
        self.image_format = image_format
        self.orientation = "portrait" if self.height > self.width else "landscape"

    def __str__(self):
        return "Image({}, {}x{}, {}, {}, {}).".format(self.name, self.height, self.width, self.size_bytes,
                                                      self.image_format, self.orientation)
