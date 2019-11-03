from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'edit/$', views.editcat,name='editcat'),
    re_path(r'done/$', views.submitcategory,name='submitcategory'),
    # re_path(r'submitcategory/submitcategory/$', views.submitcategory,name='editcat'),
    path('', views.index,name='index'),
]
