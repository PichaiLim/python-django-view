from django.http import HttpResponse

def home(requrest):
    return HttpResponse("Hello Index View")