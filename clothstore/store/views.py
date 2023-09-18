from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/nosotros.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contacto.html'

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'

class ProductIndexView(View):
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Drots"
        viewData["subtitle"] = "Lista de productos"
        viewData["clothes"] = Clothes.objects.all()

        return render (request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        # Miramos si es valido el id
        try:
            product_id = id
            if product_id < 1:
                raise Exception("Invalid ID")
        except:
            return redirect(reverse('tienda'))
        
        viewData = {}
        product = get_object_or_404(Clothes, pk=product_id)
        viewData["title"] = product.name + " - Drots"
        viewData["product"] = product

        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    class Meta:
        model = Clothes
        fields = ['name', 'price', 'color', 'description']
    
class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Crear producto - Drots"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, "./products/p_created.html")
        else:
            viewData = {}
            viewData["title"] = "Crear producto - Drots"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class LoginView(TemplateView):
    template_name = 'pages/login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        # Check if user exists
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login successful")
            return redirect(reverse('dashboard'))
        else:
            return redirect(reverse('login'), {'error': 'Usuario o contraseña incorrectos'})

class DashboardView(TemplateView):
    template_name = 'pages/dashboard.html'

class CreateView(TemplateView):
    template_name = 'pages/create.html'

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))