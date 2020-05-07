from django.core.files import File
from PIL import Image
from io import BytesIO


def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO()
    # save image to BytesIO object
    #im.save(im_io, 'JPEG', quality=70)
    # create a django-friendly Files object
    size = 800, 800
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(im_io, 'JPEG')
    new_image = File(im_io, name=image.name)
    return new_image
