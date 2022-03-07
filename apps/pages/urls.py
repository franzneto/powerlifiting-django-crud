
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from apps.train.views import *

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('train/add/', add_train, name='add_train'),
]
