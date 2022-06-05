from django.db import models


class Setting(models.Model):
    sitename= models.CharField(max_length=50,null=True, verbose_name='site name')
    siteurl= models.CharField(max_length=50,null=True, verbose_name='site url')
    ismain= models.BooleanField(verbose_name='main setting',null=True)
    email1= models.EmailField(max_length=50,null=True, verbose_name='email1')
    address1= models.CharField(max_length=50,null=True, verbose_name='address1')
    phone1= models.CharField(max_length=50,null=True, verbose_name='phone1')
    email2= models.CharField(max_length=50,null=True, verbose_name='email2')
    address2= models.CharField(max_length=50,null=True, verbose_name='address2')
    phone2= models.CharField(max_length=50,null=True, verbose_name='phone2')
    copyright= models.TextField(verbose_name='copy right',null=True)

    def __str__(self):
        return self.sitename

