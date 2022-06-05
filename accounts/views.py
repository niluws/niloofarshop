from django.shortcuts import render,redirect,reverse
from django.utils.crypto import get_random_string
from django.views import View
from .models import User
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm


class register(View):

    def get(self, request):
        registerForm = RegisterForm(request.POST)
        return render(request, 'accounts/register.html', {'registerForm': registerForm})

    def post(self, request):
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            email = registerForm.cleaned_data.get('email')
            password = registerForm.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email).exists()
            if user is not None:
                new_user = User(
                    is_active=False,
                    active_code=get_random_string(4),
                    username=email,
                    email=email
                )
                new_user.set_password(password)
                new_user.save()
                return redirect(reverse('login'))
            else:
                print('email exist')
                redirect(reverse('register'))
        else:print('password not the same')
        return render(request, 'accounts/register.html', {'registerForm': registerForm})


class activation(View):
    def get(self, request, slugcode):
        user: User = User.objects.filter(active_code__iexact=slugcode).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.active_code = get_random_string(4)
                user.save()
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
