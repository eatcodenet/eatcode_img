class Image:
    """ Simple Image with basic attributes """

    def __init__(self, name, height, width, format='Unknown'):
        self.name = name
        self.height = height
        self.width = width
        self.format = format

    def __str__(self):
        return "Image({}, {}x{}, {}).".format(self.name, self.height, self.width, self.format)
