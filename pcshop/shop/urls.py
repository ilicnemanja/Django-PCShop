from django.urls import path
from shop.views import HomeView, ProductDetailView, CategoryLaptopView, CategoryDesktopView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('pocetna/', HomeView.as_view(), name="home"),
    path('<str:category>/proizvod/<int:id>', ProductDetailView.as_view(), name="product_detail"),
    path('prenosni-racunari/', CategoryLaptopView.as_view(), name="product_laptop"),
    path('desktop-racunari/', CategoryDesktopView.as_view(), name="product_pc"),
]
