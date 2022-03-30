from django.urls import path
from .views import (
    TrainCreateView,
    TrainListView,
    TrainUpdateView,
    TrainDeleteView,
    TrainIndexTemplateView,
)

app_name = "train"

urlpatterns = [
    path("create/", TrainCreateView.as_view(), name="create_train"),  # C
    path("", TrainListView.as_view(), name="read_train"),  # R
    path("update/<int:pk>", TrainUpdateView.as_view(), name="update_train"),  # U
    path("delete/<int:pk>/", TrainDeleteView.as_view(), name="delete_train"),  # D
]
