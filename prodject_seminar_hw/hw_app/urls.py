from django.urls import path
#from . import views
from .views import index, about, creat_user, get_all_users, get_all_products, get_orders_user, get_products_user


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('create_user/', creat_user, name='create_user'),
    #path('orders_user/<int:num>/', orders_user, name='orders_user'),
    # path('delete_user/', views.delete_user, name='delete_user'),
    path('get_all_users/', get_all_users, name='get_all_users'),
    path('get_orders_user/', get_orders_user, name='get_orders_user'),
    path('get_orders_user/<int:customer_id>', get_orders_user, name='get_orders_user'),
    # path('create_product/', views.creat_product, name='create_product'),
    # path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    path('get_all_products/', get_all_products, name='get_all_products'),
    path('get_products_user/<int:customer_id>/<int:period>', get_products_user, name='get_products_user'),
    path('get_products_user/<int:customer_id>/', get_products_user, name='get_products_user'),
    path('get_products_user/', get_products_user, name='get_products_user'),


]