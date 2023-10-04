from uuid import uuid4
import os

def path_and_rename(instance, filename):
    upload_to = "properties/"
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)