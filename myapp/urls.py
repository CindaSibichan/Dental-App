from django.urls import path
from . import views

urlpatterns = [
    path('',views.LoginPageView.as_view(), name = "login"),
    path('dashboard/',views.dashboard , name='dashboard'),
    path('delete/<int:pk>/',views.delete_hospital , name="delete"),
    path('edit/',views.edit_hospital, name="edit_hospital"),
    path('block/<int:pk>/',views.block, name="block"),
    path('unblock/<int:pk>/',views.unblock , name="unblock"),
    path('expiring-soon/',views.expiring_soon , name="expiring-soon"),
    # path('delete-expiringsoon/<int:pk>/' ,views.delete_expiringsoon , name="delete-expiring"),
    path('blocked/',views.block_hospital , name="blocked-hospital"),
    path('expired/',views.expired , name="expired"),
    path('renew/<int:pk>/',views.renew_hospital , name="renew"),
    path('logout/',views.logout, name="logout"),
    
]