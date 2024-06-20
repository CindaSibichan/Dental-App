from django.db import models
from datetime import timedelta,datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
TYPE_CHOICES = [
      ('Select a type', 'Select a type'),
        ('Permanent', 'Permanent'),
        ('Temporary', 'Temporary'),
       
    ]
 
class Hospital(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False)
    phone = models.CharField(max_length=10 , null=False , blank=False)
    email = models.EmailField(null=False, blank=False)
    subscript = models.CharField(max_length=13 , choices=TYPE_CHOICES)
    no_of_days = models.IntegerField(null=True, blank=True,default=0)
    amount = models.CharField(max_length=200,null=True, blank=True,default='0')
    registration_date = models.DateField(null=True, blank=True)
    renewal_date = models.DateField(null=True, blank=True)
    is_renew = models.BooleanField(default=False)

@receiver(pre_save, sender=Hospital)
def set_validity_date(sender, instance, **kwargs):
    
    if instance.pk:  
        previous_instance = sender.objects.get(pk=instance.pk)
        # Only update validity_date if it was changed
        if instance.renewal_date!= previous_instance.renewal_date:
            instance.renewal_date = instance.registration_date + timedelta(days=365)
    else:  # This means the instance is being saved for the first time
        instance.renewal_date = instance.registration_date + timedelta(days=365)

        
def __str__(self):
    return self.name