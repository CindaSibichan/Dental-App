from django.urls import path
from . import views

urlpatterns = [
    path('',views.LoginPageView.as_view(), name = "login"),
    path('dashboard/',views.dashboard , name='dashboard'),
    path('delete/<int:pk>/',views.delete_hospital , name="delete"),
    path('logout/',views.logout, name="logout"),
    



]