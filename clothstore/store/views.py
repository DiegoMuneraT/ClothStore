from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from .models import *
from django.urls import reverse

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
        viewData["products"] = Product.objects.all()

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
        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.category + " - Drots"
        viewData["product"] = product

        return render(request, self.template_name, viewData)
