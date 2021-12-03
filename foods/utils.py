import os
from uuid import uuid4

from deufood import settings

def random_filename(instance, filename: str):
    ext = filename.split('.')[-1]

    return '{}.{}'.format(uuid4().hex, ext)
