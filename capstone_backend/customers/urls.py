from django.urls import path
from customers import views

urlpatterns = [
    path('profile/', views.user_profile),
    path('getall/', views.get_all_customers)
]