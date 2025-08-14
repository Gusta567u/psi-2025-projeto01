from django.shortcuts import render

def index(request):

    return render(request, 'blog/index.html')

def jogadores(request):

    return render(request, 'blog/jogadores.html')


def sobre(request):

    return render(request, 'blog/sobre.html')
