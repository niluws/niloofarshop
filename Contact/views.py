from django.shortcuts import render
from django.views import View
from .models import ContactModel
from .forms import ContactForm
from  siteSetting.models import Setting
class Contact(View):
    def get(self,request):
        site: Setting = Setting.objects.filter(ismain=True).first()

        contactform = ContactForm()
        return render(request, 'Contact/Contact.html', {'contactform': contactform,'site':site})
    def post(self,request):
        site: Setting = Setting.objects.filter(ismain=True).first()

        contactform = ContactForm(request.POST)
        print(request.POST)
        if contactform.is_valid():
            sql = ContactModel(
                name=contactform.cleaned_data.get('name'),
                email=contactform.cleaned_data.get('email'),
                subject=contactform.cleaned_data.get('subject'),
                message=contactform.cleaned_data.get('message'),

            )
            sql.save()
        return render(request, 'Contact/Contact.html', {'contactform': contactform,'site':site})

