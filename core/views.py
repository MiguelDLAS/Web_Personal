from django.shortcuts import render, HttpResponse


# Aqui van mis vistas 
def home(request):
    return render(request, "core\home.html")

def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core\contact.html")