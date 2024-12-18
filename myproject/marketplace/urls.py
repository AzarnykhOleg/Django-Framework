from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('client_orders/', views.client_orders, name='client_orders'),
    path('client_orders/<int:client_id>', views.client_orders, name='client_orders'),
    path('upload_immage/', views.upload_immage, name='upload_immage'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
]
