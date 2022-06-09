from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from post_detail.models import Information,Category
from siteSetting.models import Setting
from .models import Slider
class home(ListView):
    template_name = 'home.html'
    model = Information
    context_object_name = 'information'
    paginate_by = 1
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(home, self).get_context_data()
        query = Information.objects.all()
        product: Information = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['end_price']=self.request.GET.get('end_price') or db_max_price
        return context
    def get_queryset(self):
        query=super(home,self).get_queryset()
        request:HttpRequest=self.request
        end_price= request.GET.get('end_price')
        category_name = self.kwargs.get('cat')
        if category_name is not None:
            query = query.filter(cat__cat__iexact=category_name)
        if end_price is not None:
            query=query.filter(price__lte=end_price)
        return query

def header(request):
    return render(request,'shared/header_parsial.html')
def footer(request):
    site:Setting=Setting.objects.filter(ismain=True).first()
    return render(request,'shared/footer_parsial.html',{'site':site})


def navbar(request:HttpRequest):
    nav_category=Category.objects.prefetch_related('category_set').filter(is_active=True)
    Slide=Slider.objects.all()
    return render(request,'shared/navbar_parsial.html',{'nav_category':nav_category,'Slide':Slide})

def other_navbar_parsial(request):
    nav_category = Category.objects.prefetch_related('category_set').filter(is_active=True)
    info = Information.objects.all()
    return render(request,'shared/other_navbar_parsial.html',{'nav_category':nav_category,'info':info})

