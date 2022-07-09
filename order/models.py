from django.db import models
from accounts.models import User
from post_detail.models import Information
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    payment_date = models.DateField(null=True, blank=True)
    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount

    def __str__(self):
        return str(self.user)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Information, on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.IntegerField()

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)


# Create your models here.
