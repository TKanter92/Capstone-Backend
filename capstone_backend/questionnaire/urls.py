from django.urls import path
from questionnaire import views

urlpatterns = [
    path('', views.user_style),
    path('allquestionnaires/', views.get_all_questionnaires)
]