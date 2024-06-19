from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from . forms import *
# Create your views here.

class LoginPageView(View):
    def get(slef, request):
        form = LoginForm()
        return render(request, 'authorization/login.html', {'form': form})
    def post(self , request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request , user)
                return JsonResponse({'success':'True' , 'username':user.username})
            else:
                return JsonResponse({'succes':'False'}, status = 401)
        else:
            return JsonResponse({'succes':'False' ,'errors':form.errors} , status = 400)    


def dashboard(request):
    return render(request , 'index.html' )
