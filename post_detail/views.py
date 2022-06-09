from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView

from utils.http_service import get_client_ip
from .models import Information, ProductVisit


class detail(DetailView):
    template_name = 'post_detail/detail.html'
    model = Information
    context_object_name = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()

        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()
        # a=Information.objects.all()
        context['visit'] = ProductVisit.objects.filter()


        return context
