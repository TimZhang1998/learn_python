from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'urls'

urlpatterns = [
    # login
    url(r'^login/$', login, {'template_name': '../templates/users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]