https://simathapa111.medium.com/how-to-upload-a-csv-file-in-django-3a0d6295f624


#How to upload a CSV file in Django?



The CSV file also called as Comma Separated Values file is a plain-text data that are represented in a tabular format parted by a comma.
It can be created using a text editor like Notepad in Windows or vim in Linux. Occasionally, the CSV file is created by exporting a spreadsheet or database file that collected the data.
An Example of CSV file is as follows:
user.csv file
```
Name,Email,Address,Phone
Sima,simathapa111@gmail.com,Nadipur,98148212416
Gita,geeta12@outlook.com,Pokhara,+97789954742
```
If the data itself has a comma in it, we can separate it by using double quotes “…,… ”. Such as:
userprofile.csv file
```
Name,Email,Address,Phone,Profile
Sima,simathapa111@gmail.com,Nadipur,98148212416,"She is a developer, researcher and food-lover"
Gita,geeta12@outlook.com,Pokhara,+97789954742,"Geeta is a teacher, she loves to play and dance."
```
Let’s upload a simple CSV file in the Django application.
First, create a project name file
```
$ django-admin startproject csv
$ cd csv
$ python manage.py startapp csvfile
```
Now, add the csvfile app in INSTALLED_APPS of settings.py file. Add the code to create a model name Profile.
```
from django.db import models
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150,unique=True)
    profile = models.TextField()
    def __str__(self):
        return self.name
```
Register our model in the admin.py file:
```
from django.contrib import admin
# Register your models here.
from .models import Profile
admin.site.register(Profile)
```
Let’s migrate our model:
```
$ python manage.py makemigrations csvfile
$ python manage.py migrate
```
Now, let’s write on our views.py file to create a function-based view:
```
import csv, io
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
# one parameter named request
def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Profile.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            name=column[0],
            email=column[1],
            address=column[2],
            phone=column[3],
            profile=column[4]
        )
    context = {}
    return render(request, template, context)
```
Create a templates folder in the root directory and a new HTML file named profile_upload.html
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
# Add the TEMPLATE_DIR in the TEMPLATES:
'DIRS': [TEMPLATE_DIR, ],
profile_upload.html file
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {% if messages %}
        {% for message in messages %}
            <div>
<!--                | means OR operator-->
                <strong>{{message|safe}}</strong>
            </div>
        {% endfor %}
    {% else %}
    {{order}}
    <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <label for="file1"> Upload a file</label>
        <input type="file" id="file1" name="file">
        <small>Only accepts CSV files</small>
        <button type="submit">Upload</button>
    </form>
    {% endif %}
    {% for profile in profiles %}
    {{profile.name}}
    {% endfor %}
</body>
</html>
```
Add the path in the file/urls.py which is the main URL file:
```
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from csvfile.views import profile_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-csv/', profile_upload, name="profile_upload"),
]
```
Now, create a new test.csv file and try to upload it:
test.csv file
```
name,email,address,phone,profile
Sima,simathapa111@gmail.com,Nadipur,+14151234567.,"She is a developer, researcher and food-lover."
Gita,geeta12@outlook.com,Pokhara,(415) 123-4567,"Geeta is a teacher, she loves to play and dance."
Ram,ram123@gmail.com,Kathmandu,17735356563,"Ram delivers food."
```
This blog has been solely for the practice purpose. I would like to mention some references which helped me to understand the CSV file and uploading feature.
References and credits:

[Free code camp](https://www.freecodecamp.org/news/what-is-a-csv-file-and-how-to-open-the-csv-file-format/)

[Master Code Online](https://www.youtube.com/watch?v=BppyfPye8eo&feature=youtu.be)

[Computer Hope](https://www.computerhope.com/issues/ch001356.htm)