from django.urls import path
from . import views

urlpatterns = [
    path('submitcategory/', views.submitcategory,name='submitcategory'),
    path('', views.index,name='index'),
]
