from django.shortcuts import render , redirect ,get_object_or_404 ,reverse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from datetime import timedelta
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
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


# dashboard
@login_required(login_url='login')
def dashboard(request):
    start_year_str = request.GET.get('startYear')
    end_year_str = request.GET.get('endYear')
    query = request.GET.get('query')
    hospitals = Hospital.objects.filter(is_blocked=False).order_by('id')
    if not (start_year_str or end_year_str or query):
        hospitals = Hospital.objects.filter(is_blocked=False).order_by('id')
    else:
        start_year = int(start_year_str) if start_year_str else None
        end_year = int(end_year_str) if end_year_str else None    

        if query:
            hospitals = hospitals.filter(name__icontains=query) 
        elif start_year and end_year:
            hospitals = Hospital.objects.filter(Q(registration_date__year__range=[start_year, end_year])).order_by('id') 
        else:
            hospitals = Hospital.objects.filter(is_blocked=False).order_by('id')


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


# Edit hospitals
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


# delete hospital
@login_required(login_url='login')
def delete_hospital(request, pk):
    hospital = get_object_or_404(Hospital, id=pk)
    hospital.delete()
    return redirect("dashboard")


# block
@login_required(login_url='login')
def block(request,pk):
    if request.method == 'POST':
        hospital = Hospital.objects.get(pk=pk)
        hospital.is_blocked = True
        hospital.save()
        return redirect(reverse('blocked-hospital'))
    

# Expiring soon
@login_required(login_url='login')
def expiring_soon(request):
    hospitals = Hospital.objects.all()
    query = request.GET.get('query')
    expiring_soon_hospitals = []

    current_date = timezone.now().date()

    if query:
        
        hospitals = hospitals.filter(name__icontains=query)

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

    return render(request, 'expiring_soon.html', {'hospital_list': expiring_soon_hospitals ,'query':query})



# Details of blocked hospitals
@login_required(login_url='login')
def block_hospital(request):
    blocked_hospitals = Hospital.objects.filter(is_blocked =True)
    query = request.GET.get('query')

    if query:
        
        blocked_hospitals = blocked_hospitals.filter(name__icontains=query)
    for hospital in blocked_hospitals:
       
        if hospital.renewal_date:
            hospital.is_renewed = hospital.renewal_date >= datetime.now().date()
        else:
            hospital.is_renewed = False 
    return render(request ,'blocked.html',{'blocked_hospitals':blocked_hospitals ,'query':query})



# unblock
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




# Expired hospitals
@login_required(login_url='login')
def expired(request):
    current_date = timezone.now().date()
    query = request.GET.get('query')
    # notification_message = None
    expired_hospitals = Hospital.objects.filter(renewal_date__lte=current_date)
    # if expired_hospitals.exists():
    #     expired_hospital_names = ', '.join(hospital.name for hospital in expired_hospitals)
    #     notification_message = f"{expired_hospital_names} expired."

        # Add message for notification modal
        # messages.success(request, notification_message)
    if query:
        
        expired_hospitals = expired_hospitals.filter(name__icontains=query)
   
    return render(request, 'expired.html', {'hospitals': expired_hospitals ,'query':query })



# renew 
def renew_hospital(request, pk):
    hospital = Hospital.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            new_renewal_date = timezone.now() + timezone.timedelta(days=365)
            hospital.renewal_date = new_renewal_date
            hospital.is_renewal_date_explicitly_set = True
            hospital.save()
            messages.success(request, f'Renewed successfully.  New renewal date: {new_renewal_date.strftime("%d/%m/%Y")}')
            return JsonResponse({
                'success': True,
                'message': 'Renewal successful',
                'new_renewal_date': new_renewal_date.strftime("%d/%m/%Y")
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request method'
        })




def payments(request):
    hospitals = Hospital.objects.filter(subscript='Permanent')
    query = request.GET.get('query')
    if query:
        
        hospitals = hospitals.filter(name__icontains=query)
    return render(request , 'payment.html',{'hospitals':hospitals ,'query':query})


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("login")
