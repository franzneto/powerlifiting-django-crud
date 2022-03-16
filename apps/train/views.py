from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import TrainForm
from .models import Train
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def create_train(request):

    if request.method == "POST":
        form = TrainForm(request.POST)
        if form.is_valid():
            form.instance.set_user(request.user)  # link the user to the train
            form.instance.calc_tonnage()  # set the tonnage
            form.save()
            return redirect("/")
        else:
            return render(request, "train/create_train.html", {"form": form})
    elif request.method == "GET":
        form = TrainForm()
        return render(request, "train/create_train.html", {"form": form})


class ReadTrain(LoginRequiredMixin, ListView):
    model = Train
    template_name = "train/read_train.html"
    context_object_name = "trains"
    paginate_by = 5

    def get_queryset(self):
        return Train.objects.filter(user=self.request.user).order_by("-date")


def delete_train(request, pk):
    train = Train.objects.get(pk=pk)
    verifie_if_user_is_owner = train.user == request.user
    if User.is_authenticated:
        if verifie_if_user_is_owner:
            train.delete()
        return redirect("/")
    else:
        return redirect("/")


def update_train(request, pk):
    if User.is_authenticated:

        train = Train.objects.get(pk=pk)
        verifie_if_user_is_owner = train.user == request.user

        if verifie_if_user_is_owner:
            if request.method == "POST":
                form = TrainForm(request.POST, instance=train)
                if form.is_valid():
                    form.instance.calc_tonnage()  # set the tonnage
                    form.save()
                    return redirect("/")
                else:
                    return render(request, "train/update_train.html", {"form": form})
            elif request.method == "GET":
                form = TrainForm(instance=train)
                return render(request, "train/update_train.html", {"form": form})
        else:
            return redirect("/")
    else:
        return redirect("/")
