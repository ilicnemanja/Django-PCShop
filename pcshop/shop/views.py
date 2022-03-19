from django.shortcuts import render
from django.views import View


class MyView(View):
    def get(self, request):
        # <view logic>
        return render(request, 'shop/home.html')
