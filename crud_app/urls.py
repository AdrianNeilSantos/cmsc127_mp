from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('profile/', views.profile, name="profile"),
    path('cart/', views.cart, name="cart"),
    path('requests/', views.requests, name="requests"),
    path('addPet/', views.addPet, name="addPet"),
    path('requestPet/', views.requestPet, name="requestPet"),
    path('pet/<str:pk>', views.pet, name="pet"),
    path('addWishlist/', views.addWishlist, name="addWishlist"),
    path('addCart/', views.addCart, name="addCart"),
    path('deletePet/<str:pk>', views.deletePet, name="deletePet"),
    path('deleteWishlist/<str:pk>', views.deleteWishlist, name="deleteWishlist"),
    path('deleteCart/<str:pk>', views.deleteCart, name="deleteCart"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),
]