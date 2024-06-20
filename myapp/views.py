from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django.contrib import auth
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
    hospitals = Hospital.objects.all()
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
        
            return render(request, 'index.html', {'hospitals': hospitals, 'form': form})
    else:
     
        form = HospitalForm()

    return render(request, 'index.html', {'hospitals': hospitals, 'form': form})


def delete_hospital(request, pk):
    doctor = Hospital.objects.get(id=pk)
    doctor.delete()
    return redirect("dashboard")





    

def logout(request):
    auth.logout(request)
    return redirect("login")
