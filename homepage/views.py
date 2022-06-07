from django.shortcuts import redirect, render
from .forms import messageform
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = messageform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sent')
        else:
            return redirect('/')
    else:
        form = messageform()
    return render(request, "index.html", {'form':form})


def sent(request):
    return render(request, "confirmation.html")