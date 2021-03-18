Storage in Dropbox Example

https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
https://github.com/zahidtokur/django-dropbox-example

Incluir no settings:

```
DROPBOX_ACCESS_TOKEN = config('DROPBOX_ACCESS_TOKEN')
DEFAULT_FILE_STORAGE = 'django_dropbox_storage.storage.DropboxStorage'
```



```
pip install dropbox
pip install pip install git+https://github.com/zahidtokur/django-dropbox-storage.git
```
