from xml.sax.handler import property_xml_string

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValueError('The maximum file size that can be uploaded is 5MB')

@deconstructible
class FileSizeValidator:
    def __init__(self, file_size_mb:int, message=None):
        self.file_size_mb = file_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f'File size must be below {self.file_size_mb}MB'
        else:
            self.__message = value

    def __call__(self,value):
        if value.size > self.file_size_mb * 5 * 1024 * 1024:
            raise ValidationError(self.message)