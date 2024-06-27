from django.urls import path
from . import views

urlpatterns = [
    path('',views.LoginPageView.as_view(), name = "login"),
    path('dashboard/',views.dashboard , name='dashboard'),
    path('delete/<int:pk>/',views.delete_hospital , name="delete"),
    path('edit/',views.edit_hospital, name="edit_hospital"),
    path('expiring-soon/',views.expiring_soon , name="expiring-soon"),
    path('delete-expiringsoon/<int:pk>/' ,views.delete_expiringsoon , name="delete-expiring"),
    path('expired/',views.expired , name="expired"),
    path('logout/',views.logout, name="logout"),
    



]