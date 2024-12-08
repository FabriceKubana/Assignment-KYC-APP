from django.urls import path
from . import views

urlpatterns = [
    # Authentication-related URLs
    path('login/', views.agent_login, name='agent_login'),
    path('logout/', views.logout_view, name='logout'),

    # KYC Home and Dashboard URLs (Grouped under kyc-home)
    path('kyc-home/', views.kyc_home, name='kyc_home'),  # KYC Home Page
    path('kyc-home/dashboard/', views.dashboard, name='dashboard'),  # Dashboard 

    # Customer-related URLs
    path('kyc-home/dashboard/customers/', views.customer_list, name='customer_list'), 
    path('kyc-home/dashboard/customers/create/', views.customer_create, name='customer_create'),  
]
