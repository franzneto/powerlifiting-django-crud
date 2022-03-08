from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import TrainForm
from .models import Train
from django.contrib.auth.models import User

# Create your views here.

def create_train(request):
    
    if request.method == 'POST':
        form = TrainForm(request.POST)
        user = request.user
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'train/create_train.html', {'form': form})
    elif request.method == 'GET':
        form = TrainForm()
        return render(request, 'train/create_train.html', {'form': form})

class ReadTrain(ListView):
    model = Train
    template_name = 'train/read_train.html'
    context_object_name = 'trains'
    paginate_by = 5

def delete_train(request, pk):
    train = Train.objects.get(pk=pk)
    if User.is_authenticated:
        if Train.user == request.user:
            train.delete()
        return redirect('/')
    else:
        return redirect('/')
