from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('cart/', ShoppingCart.as_view(), name='cart'),
    path('api/', APIPageView.as_view(), name='api'),
    path('contacto/', ContactPageView.as_view(), name='contacto'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('tienda/', ProductIndexView.as_view(), name='tienda'),
    path('tienda/<int:id>', ProductShowView.as_view(), name='product'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/create', ProductCreateView.as_view(), name='form'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('api/products/', ProductsApiView.as_view() , name='get_products'),
]