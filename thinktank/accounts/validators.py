from django.core.exceptions import ValidationError

ONE_MB = 1048576


def validate_image_size(value):
    filesize = value.size
    if filesize > (ONE_MB):
        raise ValidationError(
            "The maximum file size that can be uploaded is 2MB")
    else:
        return value
