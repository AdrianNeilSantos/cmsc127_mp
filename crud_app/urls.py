from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signIn/', views.signIn, name="signIn"),
    path('signUp/', views.signUp, name="signUp"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('cart/', views.cart, name="cart"),
    path('addPet/', views.addPet, name="addPet"),
    path('pet/<str:pk>', views.pet, name="pet"),
]