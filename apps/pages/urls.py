
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from apps.train.views import *

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('train/create/', create_train, name='create_train'),
    path('train/read/', ReadTrain.as_view(), name='read_train'),
    path('train/delete/<int:pk>/', delete_train, name='delete_train'),
]
