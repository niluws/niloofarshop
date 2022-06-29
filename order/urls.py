from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add_product_to_order'),
    path('Shopping',views.user_basket,name='Shopping_Cart')
]
