# Generated by Django 4.0.4 on 2022-06-04 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='off',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='shoplink',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
