from django.conf.urls import url
from xmlvalidator import views

app_name = 'xmlvalidator'
urlpatterns = [
    #ex: / | /xmlvalidator
    url(r'^$', views.index, name='index'),

]