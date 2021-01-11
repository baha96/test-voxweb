from django.urls import path
# from django.conf.urls import include, url

from . import views

app_name = 'task'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
]
