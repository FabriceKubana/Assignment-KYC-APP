from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm
from django.db.models import Count

# Agent Login View
def agent_login(request):
    if request.user.is_authenticated:
        return redirect('kyc_home') 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('kyc_home')  
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'kyc/login.html')

# Logout View
def logout_view(request):
    logout(request)  
    return redirect('agent_login') 

# KYC Home View
@login_required
def kyc_home(request):
    return render(request, 'kyc/kyc_home.html')  

# MapReduce function to get customer counts by gender and nationality
def map_reduce_customers():
    # Gender count
    male_count = Customer.objects.filter(gender='M').count()
    female_count = Customer.objects.filter(gender='F').count()

    # Nationality count using the values() and annotate() methods to count occurrences of each nationality
    nationality_counts = Customer.objects.values('nationality').annotate(count=Count('nationality'))

    # Convert nationality counts to a dictionary
    nationality_dict = {item['nationality']: item['count'] for item in nationality_counts}

    return {
        'M': male_count,
        'F': female_count,
        'nationality': nationality_dict  # Include nationality counts
    }

# Dashboard View
@login_required
def dashboard(request):
    # Fetch all customers
    customers = Customer.objects.all()

    # Get the most recent 5 customers
    recent_customers = Customer.objects.order_by('-created_at')[:5]

    # Perform MapReduce on customer data
    mapreduce_results = map_reduce_customers()

    # Context data to pass to the template
    context = {
        'total_count': customers.count(),
        'male_count': customers.filter(gender='M').count(),
        'female_count': customers.filter(gender='F').count(),
        'customers': customers,
        'recent_customers': recent_customers,
        'mapreduce_results': mapreduce_results,  # MapReduce result to show on dashboard
    }

    return render(request, 'kyc/dashboard.html', context)

# Customer List View
@login_required
def customer_list(request):
    customers = Customer.objects.all()  # Fetch all customers
    return render(request, 'kyc/customer_list.html', {'customers': customers})

# Customer Create View
@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  # Save the customer data
            messages.success(request, 'Customer added successfully!')
            return redirect('dashboard')  # Redirect to dashboard after adding
    else:
        form = CustomerForm() 
    return render(request, 'kyc/customer_form.html', {'form': form})
