from django.urls import path
from . import views
urlpatterns = [
    path('<slug:slug>',views.detail.as_view(),name='detail')
]
