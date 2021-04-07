#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from storagessnp.forms import DocumentForm
from storagessnp.models import Document


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'storagessnp/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'storagessnp/simple_upload.html')


def home(request):
    documents = Document.objects.all()
    return render(request, 'storagessnp/home.html', {'documents': documents})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'storagessnp/model_form_upload.html', {
        'form': form
    })