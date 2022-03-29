from django.views.generic.list import ListView
from django.core.exceptions import PermissionDenied
from .forms import TrainForm
from .models import Train
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import UpdateView, CreateView, DeleteView


class TrainCreateView(LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = "train/create_train.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.set_user(self.request.user)  # link the user to the train
        form.instance.calc_tonnage()  # set the tonnage
        return super().form_valid(form)


class TrainListView(LoginRequiredMixin, ListView):
    model = Train
    template_name = "train/read_train.html"
    context_object_name = "trains"
    paginate_by = 5

    def get_queryset(self):
        return Train.objects.filter(user=self.request.user)


class TrainUpdateView(LoginRequiredMixin, UpdateView):
    model = Train
    template_name = "train/update_train.html"
    fields = ["exercise", "weight", "repetitions"]
    success_url = "/"

    def get_object(self, queryset=None):
        obj = super(TrainUpdateView, self).get_object()
        if obj.user != self.request.user:
            raise PermissionDenied()
        return obj


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    template_name = "train/delete_train.html"
    success_url = "/"
    pk_url_kwarg = "pk"

    def get_object(self, queryset=None):
        obj = super(TrainDeleteView, self).get_object()
        if obj.user != self.request.user:
            raise PermissionDenied()
        return obj
