from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from clothstore.services.shirtInterface import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ShoppingCart(TemplateView):
    template_name = 'pages/cart.html'

class APIPageView(TemplateView):
    template_name = 'pages/api.html'

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
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'price', 'color', 'description', 'image']
    
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
            return redirect(reverse('dashboard'))
        else:
            viewData = {}
            viewData["title"] = "Crear producto - Drots"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'telnumber', 'comment']
        
class CommentCreateView(View):
    template_name = "pages/contacto.html"

    def get(self, request):
        form = CommentForm()
        viewData = {}
        viewData["title"] = "Crear comentario - Drots"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contacto'))
        else:
            viewData = {}
            viewData["title"] = "Crear comentario - Drots"
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

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

class ProductsApiView(View):

    def get(self, request):
        clothes = Clothes.objects.all()
        data = {
            'Products': [
                {
                    'name': clothes.name,
                    'price': clothes.price,
                    'color': clothes.color,
                    'size': clothes.size,
                    'description': clothes.description,
                }
                for clothes in clothes
            ]
        }
        return JsonResponse(data)
    
class ProductEditView(TemplateView):
    template_name = 'products/select_modify.html'

class ProductEdit(View):
    template_name = 'products/modify.html'

    def get(self, request, id):
        # Miramos si es valido el id
        try:
            product_id = id
            if product_id < 1:
                raise Exception("Invalid ID")
        except:
            return redirect(reverse('dashboard'))
        
        viewData = {}
        product = get_object_or_404(Clothes, pk=product_id)
        viewData["title"] = product.name + " - Drots"
        viewData["product"] = product

        return render(request, self.template_name, viewData)

    def post(self, request, id):
        # Miramos si es valido el id
        try:
            product_id = id
            if product_id < 1:
                raise Exception("Invalid ID")
        except:
            return redirect(reverse('dashboard'))
        
        product = get_object_or_404(Clothes, pk=product_id)
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.color = request.POST['color']
        product.description = request.POST['description']
        product.save()
        return redirect(reverse('dashboard'))

class CustomCreationView(TemplateView):
    template_name = 'pages/custom.html'

    

class CustomPreviewView(TemplateView):
    template_name = 'pages/preview.html'
    def post(self, request):
        shirt = ShirtDesign()
        modelo = Printful()
        minimalista = PokeShirt()
        option = request.POST["option_selector"]
        if request.method == 'POST' and option == 'modelo':
            textbox_value = request.POST['textbox']
            design = shirt.getDesign(textbox_value)
            mockup = modelo.createMockup(design)
            context = {
                'image_url': mockup
                }
            return render(request,'pages/preview.html', context) 
        else:
            textbox_value = request.POST['textbox']
            design = shirt.getDesign(textbox_value)
            mockup = minimalista.createMockup(design)
            context = {
                'image_url': mockup
                }
            return render(request,'pages/preview.html', context) 
            

