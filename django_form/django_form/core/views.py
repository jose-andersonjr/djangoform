from http.client import HTTPResponse
from django.shortcuts import render

from .forms import MeuFormulario

# Create your views here.
def home(request):
    form = MeuFormulario()
    context = {
        'form':form
    }
    return render(request, 'home.html', context=context)

