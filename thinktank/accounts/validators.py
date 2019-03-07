from django.core.exceptions import ValidationError
from PIL import Image

ONE_MB = 1048576
WIDTH = 200
HEIGHT = 200


def validate_image_size(value):
    filesize = value.size
    if filesize > (ONE_MB):
        raise ValidationError(
            "The maximum file size that can be uploaded is 2MB")
    else:
        return value


def validate_image_width_and_height(image):
    errors = []
    if image.width > WIDTH:
        errors.append('Width should be <= {} px.'.format(WIDTH))
    if image.height < HEIGHT:
        errors.append('Height should be <= {} px.'.format(HEIGHT))
    if image.width != image.height:
        errors.append('Width and height should be same.')
    raise ValidationError(errors)
