from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Eric Bernardes',
        })


def sobre(request):
    return render(request, 'recipes/pages/sobre.html')


def contato(request):
    return render(request, 'recipes/pages/contato.html')
