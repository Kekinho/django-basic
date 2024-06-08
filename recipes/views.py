from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Eric Bernardes',
        })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Eric Bernardes',
    })


def contato(request):
    return render(request, 'recipes/pages/contato.html')
