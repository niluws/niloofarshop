from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add_product_to_order'),
    path('Shopping', views.user_basket, name='Shopping_Cart'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
path('request-payment/', views.request_payment, name='request_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment')

]
