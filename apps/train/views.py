from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import TrainForm
from .models import Train
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ReadTrain(LoginRequiredMixin, ListView):
    model = Train
    template_name = 'train/read_train.html'
    context_object_name = 'trains'
    paginate_by = 5

    def get_queryset(self):
        return Train.objects.filter(user=self.request.user).order_by('-date')

def delete_train(request, pk):
    train = Train.objects.get(pk=pk)
    verifie_if_user_is_owner = train.user == request.user
    if User.is_authenticated:
        if verifie_if_user_is_owner:
            train.delete()
        return redirect('/train/read')
    else:
        return redirect('/')
