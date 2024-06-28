from django.shortcuts import render , redirect ,get_object_or_404 ,reverse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def dashboard(request):
    hospitals = Hospital.objects.all()
    query = request.GET.get('query')

    if query:
        
        hospitals = hospitals.filter(name__icontains=query) 

    for hospital in hospitals:
       
        if hospital.renewal_date:
            hospital.is_renewed = hospital.renewal_date >= datetime.now().date()
        else:
            hospital.is_renewed = False    
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('dashboard')
        else:
            print("form is not valid")
            print(form.errors)
        
            return render(request, 'index.html', {'hospitals': hospitals, 'form': form})
    else:
     
        form = HospitalForm()

    return render(request, 'index.html', {'hospitals': hospitals, 'form': form ,'query':query})

@login_required(login_url='login')
def edit_hospital(request):
    if request.method == 'POST':
        hospital_id = request.POST.get('hospital_id')
        print(f"Received hospital_id: {hospital_id}")
        hospital = get_object_or_404(Hospital, pk=hospital_id)
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            print("Form is valid, saving data....")
            form.save()
            return redirect('dashboard')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        print("Request method is not POST")
    return redirect('dashboard')

@login_required(login_url='login')
def delete_hospital(request, pk):
    hospital = get_object_or_404(Hospital, id=pk)
    hospital.delete()
    return redirect("dashboard")


@login_required(login_url='login')
def block(request,pk):
    if request.method == 'POST':
        hospital = Hospital.objects.get(pk=pk)
        hospital.is_blocked = True
        hospital.save()
        return redirect(reverse('blocked-hospital'))
    

@login_required(login_url='login')
def expiring_soon(request):
    hospitals = Hospital.objects.all()
    expiring_soon_hospitals = []

    current_date = timezone.now().date()

    for hospital in hospitals:
        registration_date = hospital.registration_date
        renewal_date = hospital.renewal_date

        if hospital.renewal_date:
            hospital.is_renewed = hospital.renewal_date >= datetime.now().date()
        else:
            hospital.is_renewed = False  
        
      
        if registration_date is None or renewal_date is None:
            continue
        
      
        expiring_soon_threshold = renewal_date - timedelta(days=30)
        
      
        if expiring_soon_threshold <= current_date <= renewal_date:
            expiring_soon_hospitals.append(hospital)

    return render(request, 'expiring_soon.html', {'hospital_list': expiring_soon_hospitals})

@login_required(login_url='login')
def block_hospital(request):
    blocked_hospitals = Hospital.objects.filter(is_blocked =True)
    for hospital in blocked_hospitals:
       
        if hospital.renewal_date:
            hospital.is_renewed = hospital.renewal_date >= datetime.now().date()
        else:
            hospital.is_renewed = False 
    return render(request ,'blocked.html',{'blocked_hospitals':blocked_hospitals})


@login_required(login_url='login')
def unblock(request ,pk):
    if request.method == 'POST':
        hospital = Hospital.objects.get(pk=pk)
        hospital.is_blocked = False
        hospital.save()
        return redirect(reverse('dashboard'))


 
# def delete_expiringsoon(request, pk):
#     hospital = Hospital.objects.get(id=pk)
#     hospital.delete()
#     return redirect("expiring-soon")



@login_required(login_url='login')
def expired(request):
    current_date = timezone.now().date()
    expired_hospitals = Hospital.objects.filter(renewal_date__lte=current_date)
    return render(request, 'expired.html', {'hospitals': expired_hospitals})


@login_required(login_url='login')
def renew_hospital(request , pk):
    hospital = Hospital.objects.get(pk=pk)
    if request.method == 'POST':
        new_renewal_date = timezone.now() + timezone.timedelta(days=365)
        hospital.renewal_date = new_renewal_date
        hospital.is_renewal_date_explicitly_set = True
        hospital.save()
        return redirect('dashboard')




@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("login")
