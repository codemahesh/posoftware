from django.urls import path
from . import views



urlpatterns = [
     #---------------------Dashboard----------------------------------
    path('',views.dashboard_show, name='showdashboard'),
    #--------------------- Customer  Urls------------------------------
    path('customer/',views.customer_show, name='showcustomer'),
    path('customer/add/',views.customer_add, name='addcustomer'),
    path('customer/update/<int:id>/',views.customer_update, name='updatecustomer'),
    path('customer/delete/<int:id>/',views.customer_delete, name='deletecustomer'),


    #---------------------Customer PO urls------------------------------
    path('customerpo/', views.customerpo_show, name='showcustomerpo'),
    path('customerpo/add/',views.customerpo_add,
         name='addcustomerpo'),
    path('customercode/',
         views.get_customer_code, name='customercode'),
    path('getcustomerdetail',views.get_customer_detail, name='getcustomerdetail'),
    
    path('customerpo/update/<int:id>/',views.customerpo_update, name='updatecustomerpo'),
    path('customerpo/delete/<int:id>/',views.customerpo_delete, name='deletecustomerpo'),
]