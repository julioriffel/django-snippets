#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.urls import path

from csvfile import views

appname = 'csvimport'
urlpatterns = [
    path('', views.profile_upload, name='profile_upload'),
    path('pd', views.pandas_upload, name='pd_upload'),
]
