from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to homepage!")
def homeWithName(request,nom):
    return HttpResponse(f"Welcome to homepage {nom}!")