from user.models import UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from product.models import Category
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('User App')

def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id = current_user.id)
            request.session['userimage'] = userprofile.image.url

            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Login error! Username or password is incorrect.')
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login_form.html', context)

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_form(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'register_form.html', context)