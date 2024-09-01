from django.urls import path

from . import views

app_name = 'aacounts'

urlpatterns = [
    path('signup/' , views.SignupVIew.as_view() , name = 'signup'),
]
