from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Agent, Customer

# Custom Admin for Agent model
class CustomAgentAdmin(UserAdmin):
    model = Agent
    list_display = ('username', 'name', 'email', 'auuid', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'email', 'auuid')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'auuid', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'name', 'email', 'auuid')
    ordering = ('username',)

# Register Agent model with CustomAgentAdmin
admin.site.register(Agent, CustomAgentAdmin)

# Custom Admin for Customer model
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'date_of_birth',
        'gender',
        'id_number',
        'id_type',
        'nationality',
        'created_at',
    )
    list_filter = ('gender', 'id_type', 'nationality') 
    search_fields = ('first_name', 'last_name', 'id_number') 

# Register Customer model with CustomerAdmin
admin.site.register(Customer, CustomerAdmin)
