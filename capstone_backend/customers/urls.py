from django.urls import path
from customers import views

urlpatterns = [
    path('profile/', views.user_profile)
]