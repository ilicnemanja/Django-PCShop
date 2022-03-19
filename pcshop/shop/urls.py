from django.urls import path
from shop.views import MyView

urlpatterns = [
    path('', MyView.as_view()),
    path('home/', MyView.as_view()),
]
