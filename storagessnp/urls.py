#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.urls import path

from storagessnp import views

appname = 'upload'
urlpatterns = [
    path('', views.home, name='home'),
    path('simple/', views.simple_upload, name='simple_upload'),
    path('uploads/form/', views.model_form_upload, name='model_form_upload'),
]
