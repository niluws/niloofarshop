from django.db import models
class ContactModel(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    class Meta:
        verbose_name='message'
        verbose_name_plural='messages'
    def __str__(self):
        return self.subject
# Create your models here.
