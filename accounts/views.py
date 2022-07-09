from django.http import Http404
from django.shortcuts import render,redirect,reverse
from django.utils.crypto import get_random_string
from django.views import View
from .models import User
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm
from utils.email_service import send_email

class register(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'accounts/register.html', {'registerForm': register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'email is exist')
                redirect(reverse('register'))
            else:
                new_user = User(
                    email=user_email,
                    active_code=get_random_string(47),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                send_email('activation', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return redirect(reverse('login'))

        return render(request, 'accounts/register.html', {'registerForm': register_form})



class activation(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(active_code__iexact=active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.active_code = get_random_string(47)
                user.save()
                return redirect(reverse('login'))
            else:
                print('its activated')
        else:
            print('code is broken')

        return redirect(reverse('login'))


class loginView(View):

    def get(self, request):
        loginForm = LoginForm(request.POST)
        return render(request, 'accounts/login.html', {'loginForm': loginForm})

    def post(self, request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            email = loginForm.cleaned_data.get('email')
            password = loginForm.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                print(User.is_active)
                if not user.is_active:
                    return redirect(reverse('login'))
                else:
                    is_password_correct = user.check_password(password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home'))
                    else:
                        return redirect(reverse('login'))
            else:
                return redirect(reverse('register'))

        return render(request, 'accounts/login.html', {'loginForm': loginForm})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
