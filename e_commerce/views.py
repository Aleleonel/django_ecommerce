from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


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
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contato",
        "content": "Informe seus dados para contato",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # Apenas uma verificação no terminal
    ###if request.method == 'POST':
        #print(request.POST)
    return render(request, "contact/contact_page.html", context)
    