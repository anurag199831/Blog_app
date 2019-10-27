from django.urls import path
from . import views


urlpatterns = [
    path('postsubmit/', views.postsubmit,name='postsubmit'),
    path('', views.index,name='index'),
]
