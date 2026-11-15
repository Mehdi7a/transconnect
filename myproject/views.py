from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def homeWithName(request, nom):
    return render(request, 'home.html', {'nom': nom})