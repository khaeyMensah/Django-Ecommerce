from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'home': index
    }
    return render(request, 'core\index.html', context)
