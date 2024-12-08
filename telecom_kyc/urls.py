from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls import handler404, handler500

# Redirect root to login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('kyc/', include('kyc.urls')), 
    path('', lambda request: redirect('agent_login')), 
]

# Custom error handling views
handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

