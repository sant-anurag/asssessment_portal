from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line
    path('take/<int:exam_id>/', views.take_exam, name='take_exam'),
]
