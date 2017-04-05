import os
import piexif
from wand.image import Image
from wand.color import Color

from gallery.file_modules import FileModule
from gallery.util import hash_file

class GIFFile(FileModule):

    def __init__(self, file_path):
        FileModule.__init__(self, file_path)
        self.mime_type = "image/gif"

        self.generate_thumbnail()
        print("START GIF")


    def generate_thumbnail(self):
        print("GEN THUMB GIF")
        self.thumbnail_uuid = hash_file(self.file_path) + ".jpg"

        with Image(filename=self.file_path) as img:
            print(img.__dict__)
            with img.clone() as image:
                size = image.width if image.width < image.height else image.height
                image.crop(width=size, height=size, gravity='center')
                image.resize(256, 256)
                image.background_color = Color("#EEEEEE")
                image.format = 'jpeg'
                image.save(filename=os.path.join("/gallery-data/thumbnails",
                    self.thumbnail_uuid))
