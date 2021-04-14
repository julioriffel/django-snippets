#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.urls import path

from apptemplate import views

appname = 'csvimport'
urlpatterns = [
    path('01/', views.page01, name='page01'),
    path('02/', views.page02, name='page02'),

]
