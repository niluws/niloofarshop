from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView

from .models import Information, ProductVisit


class detail(DetailView):
    template_name = 'post_detail/detail.html'
    model = Information
    context_object_name = 'slug'


