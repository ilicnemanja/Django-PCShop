from django.urls import path
from shop.views import *

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name="home"),
    path('pocetna/', HomeView.as_view(), name="home"),

    # product detail view
    path('<str:category>/proizvod/<int:id>',
         ProductDetailView.as_view(), name="product_detail"),

    # product by category view
    path('prenosni-racunari/', CategoryLaptopView.as_view(), name="product_laptop"),
    path('desktop-racunari/', CategoryDesktopView.as_view(), name="product_pc"),

    # register view
    path('registracija/', RegisterView.as_view(), name="register"),

    # login view
    path('prijava/', LoginView.as_view(), name="prijava"),
]
