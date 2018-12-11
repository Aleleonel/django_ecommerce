from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Pagina Principal",
        "content": "Esta é a pagina principal"
    }
    return render(request , "home/home_page.html", context)

def about_page(request):
    context = {
        "title": "Pagina Sobre",
        "content": "Esta é a página Sobre"
    }
    return render(request, "about/about_page.html", context)

def contact_page(request):
    context = {
        "title": "Contato",
        "content": "Informe seus dados para contato"
    }
    if request.method == 'POST':
        print(request.POST)
    return render(request, "contact/contact_page.html", context)
    