from django import forms
import re
from .models import *
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 225 , widget = forms.TextInput (attrs={'placeholder': 'Enter your username', 'id': 'username', 'class': 'px-10 py-2 border-2 border-gray-400  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500  '}))
    password = forms.CharField( widget = forms.PasswordInput (attrs={'placeholder': 'Enter your password', 'id': 'password', 'class': 'px-10 py-2 border-2 border-gray-400  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500  '}))

    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username or not password:
            raise ValidationError('Please enter both username and password.')

        username_pattern = r'^[a-zA-Z0-9_]{3,16}$'
        password_pattern = r'^(?=.*\d)(?=.*[a-zA-Z]).{8,}$'

        if not re.match(username_pattern, username):
            raise ValidationError(
                'Invalid username .')

        if not re.match(password_pattern, password):
            raise ValidationError(
                'Invalid password .')

        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            raise ValidationError('Invalid username or password.')

        return cleaned_data 
    

# def validate_email(value):
#     email_pattern = r'^[a-z][a-z0-9._%+-]*@[a-z0-9.-]+\.[a-z]{2,}$'
#     if not re.match(email_pattern, value):
#         raise ValidationError("Please enter the requested format.")



class HospitalForm(forms.ModelForm):
    # email = forms.EmailField(
    #     validators=[validate_email],
    #     widget=forms.EmailInput(attrs={
    #         'pattern': r'^[a-z][a-z0-9._%+-]*@[a-z0-9.-]+\.[a-z]{2,}$',
    #         'class': 'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm'
    #     })
    # )
    # registration_date = forms.DateField(
    #     widget=forms.DateInput(format='%d/%m/%Y',
    #     attrs={ 'class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 pr-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm ','type':'date'}),
    #     input_formats=['%d/%m/%Y', '%Y-%m-%d'],
    #     required=False
        
    # )

    class Meta:
        model = Hospital
        fields = [ 'name' , 'phone' ,'email' ,'subscript' , 'no_of_days' ,'amount','registration_date' ]
        widgets = {
            'name' : forms.TextInput(attrs={'pattern': '^[a-zA-Z ]+$','class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  '}),
            'phone':forms.TextInput(attrs={'pattern': r'\d{10}', 'class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  '}),
            'email':forms.EmailInput(attrs={ 'class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  '}),
            'subscript':forms.Select(attrs={ 'class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm '}),
            'no_of_days':forms.NumberInput(attrs={'class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  '}),
            'amount':forms.NumberInput(attrs={ 'class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm  '}),
            'registration_date':forms.DateInput(attrs={ 'class':'form-control block w-[60vw] sm:w-[35vw] h-[6vh] py-1 lg:py-1 pl-4 pr-4 placeholder-gray-500 border border-gray-300 rounded text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-xs lg:text-sm ', 'type':'date' })
}
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Set initial value for registration_date if not provided by instance
    #     if not self.instance.pk:
    #         self.initial['registration_date'] = timezone.now().date()  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set registration_date as not required if subscript is 'Temporary'
        if self.instance and self.instance.subscript == 'Temporary':
            self.fields['registration_date'].required = False
            self.fields['registration_date'].widget.attrs['disabled'] = True 
    

    def clean_registration_date(self):
        # Custom clean method for registration_date if needed
        registration_date = self.cleaned_data.get('registration_date')
        if registration_date and self.instance.subscript == 'Temporary':
            # Clear the value if subscript is 'Temporary' and field is not required
            return None
        return registration_date
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Set registration_date if not provided and subscript is not 'Temporary'
        if not instance.registration_date and instance.subscript != 'Temporary':
            instance.registration_date = timezone.now().date()
        if commit:
            instance.save()
        return instance

    # def __init__(self, *args, **kwargs):
    #     super(HospitalForm, self).__init__(*args, **kwargs)
    #     if self.instance and self.instance.subscript == 'Temporary':
    #         self.fields.pop('registration_date', None)  
   
