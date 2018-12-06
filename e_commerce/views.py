from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Pagina Principal",
        "content": "Esta é a pagina principal"
    }
    return render(request , "home_page.html", context)

def about_page(request):
    context = {
        "title": "Pagina Sobre",
        "content": "Esta é a página Sobre"
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    context = {
        "title": "Página de Contato",
        "content": "Esta é a página de contato"
    }
    return render(request, "contact_page.html", context)
    