"""define url patterns of learning_logs"""

from django.conf.urls import url

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),

    # topics
    url(r'^topics/$', views.topics, name='topics'),

    # a certain topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # add a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # add a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # edit a certain entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]