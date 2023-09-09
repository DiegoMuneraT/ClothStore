from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('nosotros/', AboutPageView.as_view(), name='nosotros'),
    path('contacto/', ContactPageView.as_view(), name='contacto'),
    path('blog/', BlogPageView.as_view(), name='blog'),
]