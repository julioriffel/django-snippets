from django.urls import path

from csvfile import views

appname = 'csvimport'
urlpatterns = [
    path('', views.profile_upload, name='profile_upload'),
]
