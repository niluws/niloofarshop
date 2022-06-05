from django.shortcuts import render,get_object_or_404
from .models import Information
def detail(request,slug):
    slug=get_object_or_404(Information,slug=slug)
    return render(request,'post_detail/detail.html',{'slug':slug})
