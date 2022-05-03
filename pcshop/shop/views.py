from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from .models import product


class HomeView(View):
    def get(self, request):
        all_products = product.Product.objects.all().order_by('-created')[:25]
        products_latest = product.Product.objects.all()
        laptops = product.Product.objects.all().filter(
            subcategory__category__name="Laptop računari")
        pcs = product.Product.objects.all().filter(
            subcategory__category__name="Desktop računari")
        return render(request, 'shop/home.html', context={"products": all_products, "laptops": laptops, "pcs": pcs, "products_latest": products_latest})


class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        product_subcategory = self.kwargs['subcategory']

        product_detail = get_object_or_404(
            product.Product, id=product_id, subcategory__name=product_subcategory)

        laptops = product.Product.objects.all().filter(
            subcategory__category__name="Laptop računari")
        pcs = product.Product.objects.all().filter(
            subcategory__category__name="Desktop računari")

        return render(request, 'shop/product_detail.html', context={"product": product_detail, "laptops": laptops, "pcs": pcs})


class CategoryLaptopView(View):
    def get(self, request, *args, **kwargs):
        laptops = product.Product.objects.all().filter(
            subcategory__category__name="Laptop računari")
        for_home_use = product.Product.objects.all().filter(
            subcategory__name="Za kućnu upotrebu")
        for_job = product.Product.objects.all().filter(
            subcategory__name="Za posao")
        for_gaming = product.Product.objects.all().filter(
            subcategory__name="Za gaming")
        with_intel = product.Product.objects.all().filter(
            subcategory__name="Sa Intel procesorom")
        with_amd = product.Product.objects.all().filter(
            subcategory__name="Sa AMD procesorom")

        return render(request, 'shop/product_laptop.html', context={"laptops": laptops, "for_home_use": for_home_use, "for_job": for_job, "for_gaming": for_gaming, "with_intel": with_intel, "with_amd": with_amd})


class CategoryDesktopView(View):
    def get(self, request, *args, **kwargs):
        pcs = product.Product.objects.all().filter(
            subcategory__category__name="Desktop računari")
        pc_intel = product.Product.objects.all().filter(
            subcategory__name="Intel procesor")
        pc_amd = product.Product.objects.all().filter(
            subcategory__name="AMD procesor")
        return render(request, 'shop/product_pc.html', context={"pcs": pcs, "pc_intel": pc_intel, "pc_amd": pc_amd})


class CategoryComponentsView(View):
    def get(self, request, *args, **kwargs):
        processors = product.Product.objects.all().filter(
            subcategory__name="Procesori")
        motherboards = product.Product.objects.all().filter(
            subcategory__name="Matične ploče")
        graphics_cards = product.Product.objects.all().filter(
            subcategory__name="Grafičke karte")
        pc_ram = product.Product.objects.all().filter(
            subcategory__name="Memorije")
        ssd = product.Product.objects.all().filter(
            subcategory__name="SSD")
        housings = product.Product.objects.all().filter(
            subcategory__name="Kućišta")
        power_supply = product.Product.objects.all().filter(
            subcategory__name="Napajanje")
        coolers = product.Product.objects.all().filter(
            subcategory__name="Kuleri i oprema")
        hard_drives = product.Product.objects.all().filter(
            subcategory__name="Hard diskovi")
        return render(request, 'shop/product_comp.html', context={"processors": processors, "graphics_cards": graphics_cards, "motherboards": motherboards, "pc_ram": pc_ram, "ssds": ssd, "housings": housings, "power_supply": power_supply, "coolers": coolers, "hard_drives": hard_drives})


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shop/register.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shop/login.html')
