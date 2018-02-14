from django.conf.urls import url
from rango import views

app_name = 'rango'
urlpatterns = [
    #ex: / | /rango
    url(r'^$', views.index, name='index'),
    #ex: /rango/about
    url(r'^about/$', views.about, name='about'),
    #ex: /rango/add_category
    url(r'^add_category/$', views.add_category, name='add_category'),
    #ex: /rango/add_page
    url(r'^(?P<category_name_slug>[\w\-]+)/add_page', views.add_page, name='add_page'),
    #ex: /rango/category/Python[param]
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    #ex: /rango/register
    url(r'^register/$', views.register, name='register'),
    
    url(r'^logout/$', views.logout_view, name='logout'),
    #ex: /rango/login
    url(r'^login/$', views.user_login, name='login'),

    url(r'^restricted/$', views.restricted, name='restricted'),
]