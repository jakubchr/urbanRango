from django.conf.urls import url
from xmlvalidator import views

app_name = 'xmlvalidator'
urlpatterns = [
    #ex: / | /xmlvalidator
    url(r'^$', views.model_xml_upload, name='model_xml_upload'),
]