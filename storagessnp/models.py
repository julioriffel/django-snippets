#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.db import models


def user_directory_path(instance, filename):
    try:
        a = instance.user.id
    except:
        a = 'anoni'
    return 'user_{0}/{1}'.format(a, filename)



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path, verbose_name='aaaaaaaaaaa')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # from django_dropbox_storage.storage import DropboxStorage
    #
    # DROPBOX_STORAGE = DropboxStorage()
    # document = models.FileField(upload_to='photos', storage=DROPBOX_STORAGE)