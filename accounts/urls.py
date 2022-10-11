 
from django.urls import path
from . import views

urlpatterns = [
path('login/',views.login_view, name='login'),
path('logon/',views.login_view, name='logon'),
path('logout/',views.logout_view, name='logout')

]