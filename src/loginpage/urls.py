from django.urls import path,re_path
from . import views

urlpatterns = [
    # path('edit/', views.submitcategory,name='submitcategory'),
    # path('<slug:slug>/edit/', views.submitcategory,name='submitcategory'),
    # path('submitcategory/edit/', views.submitcategory,name='submitcategory'),
    # path('<slug:slug>', views.submitcategory,name='submitcategory'),
    # path('submitcategory/<slug:slug>', views.submitcategory,name='submitcategory'),
    re_path(r'edit/$', views.editcat,name='editcat'),
    re_path(r'edit/submitcategory/$', views.submitcategory,name='editcat'),
    path('', views.index,name='index'),
]
