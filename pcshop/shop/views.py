from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from .models import product

class HomeView(View):
    def get(self, request):
        all_products = product.Product.objects.all()
        return render(request, 'shop/home.html', context={"products": all_products})

class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        product_category = self.kwargs['category']

        all_products = product.Product.objects.all()
        product_detail = get_object_or_404(product.Product, id=product_id, category__name=product_category)
        return render(request, 'shop/product_detail.html', context={"product": product_detail, "products": all_products})
