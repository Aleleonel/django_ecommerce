from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Home",
        "content": "Seja Bem Vindo!"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Peremium"
    
    return render(request , "home/home_page.html", context)

def about_page(request):
    context = {
        "title": "Pagina Sobre",
        "content": "Esta é a página Sobre"
    }
    return render(request, "about/about_page.html", context)

def contact_page(request):
    context = {
        "title": "Página de Contato",
        "content": "Esta é a página de contato"
    }
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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    print("User Logged in")
    #print(request.user.is_authenticated)
    if form.is_valid():
        print("form.cleaned_data")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)

        #print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            # redireciona para uma pagina de sucesso
            return redirect("/")
        
        else:
            # Retona uma menssagem de erro "invalid login"
            print("login inválid")

    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request,"auth/register.html", context)




    