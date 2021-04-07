#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

import csv
import io

import pandas as pd
from django.contrib import messages
from django.shortcuts import render

from csvfile.models import Profile


def profile_upload(request):
    # declaring template
    template = "csvfile/profile_upload.html"
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


def pandas_upload(request):
    # declaring template
    context = {}
    template = "csvfile/profile_upload.html"
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

    if csv_file:
        df = pd.read_csv(csv_file)
        context['data'] = df
    else:
        messages.warning(request, f'No file to process! Please upload a file to process.')
    # data_set = csv_file.read().decode('UTF-8')
    # # setup a stream which is when we loop through each line we are able to handle a data in a stream
    # io_string = io.StringIO(data_set)
    # next(io_string)
    # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #     _, created = Profile.objects.update_or_create(
    #         name=column[0],
    #         email=column[1],
    #         address=column[2],
    #         phone=column[3],
    #         profile=column[4]
    #     )

    return render(request, template, context)
