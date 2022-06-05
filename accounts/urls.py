from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.register.as_view(),name='register'),
    path('login/',views.loginView.as_view(),name='login'),
    path('activation/<slugcode>',views.activation.as_view(),name='activation'),
    path('', views.LogoutView.as_view(), name='Logout'),

]