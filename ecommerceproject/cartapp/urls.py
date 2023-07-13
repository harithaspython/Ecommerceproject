from django.urls import path
from . import views
app_name ='cartapp'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('trash_remove/<int:product_id>/', views.trash_remove, name='trash_remove'),
]
