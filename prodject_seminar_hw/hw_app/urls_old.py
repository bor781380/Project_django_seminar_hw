from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('create_user/', views.creat_user, name='create_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),
    path('create_product/', views.creat_product, name='create_product'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    path('get_all_products/', views.get_all_products, name='get_all_products'),

]