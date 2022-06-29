from django.shortcuts import render
from django.http import HttpRequest, JsonResponse,HttpResponse
from post_detail.models import Information
from .models import Order, OrderDetail
def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get("product_id"))
    count = int(request.GET.get('count'))
    print(f'product is:{product_id} count is  {count}')
    if count < 1:
        # count = 1
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی باشد',
            'confirm_button_text': 'مرسی از شما',
            'icon': 'warning'
        })

    if request.user.is_authenticated:
        product = Information.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'added',
                'confirm_button_text': 'ok',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'not found',
                'confirm_button_text': 'thank you',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'you should be login',
            'confirm_button_text': 'login',
            'icon': 'error'
        })
def user_basket(request: HttpRequest):
    # detail_id = request.GET.get('detail_id')
    # if detail_id is None:
    #     return JsonResponse({
    #         'status': 'not_found_detail_id'
    #     })
    #
    # current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
    #                                                                                          user_id=request.user.id)
    # detail = current_order.orderdetail_set.filter(id=detail_id).first()
    #
    # if detail is None:
    #     return JsonResponse({
    #         'status': 'detail_not_found'
    #     })
    #
    # detail.delete()
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = 0
    for order_detail in current_order.orderdetail_set.all():
        total_amount += order_detail.product.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'order/user_basket.html', context)
