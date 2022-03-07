from django.shortcuts import redirect
from django.shortcuts import render
from .forms import TrainForm


# Create your views here.

def add_train(request):
    
    if request.method == 'POST':
        form = TrainForm(request.POST)
        user = request.user
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'train/add_train.html', {'form': form})
    elif request.method == 'GET':
        form = TrainForm()
        return render(request, 'train/add_train.html', {'form': form})

