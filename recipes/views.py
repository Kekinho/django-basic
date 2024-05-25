from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')


def contato(request):
    return render(request, 'recipes/pages/contato.html')


def sobre(request):
    return render(request, 'recipes/pages/sobre.html')
