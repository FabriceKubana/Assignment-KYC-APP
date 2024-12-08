from functools import reduce
from django.db.models import Count
from .models import Customer

# Map function (group customers by gender and nationality)
def map_customers(customers):
    mapped_data = []
    for customer in customers:
        # Map customers to gender and nationality
        mapped_data.append(('gender', customer.gender, 1))
        mapped_data.append(('nationality', customer.nationality, 1))
    return mapped_data

# Reduce function (aggregate by gender and nationality)
def reduce_customers(mapped_data):
    reduced_data = {
        'gender': {},
        'nationality': {}
    }

    # Process the mapped data
    for group, value, count in mapped_data:
        if group == 'gender':
            if value in reduced_data['gender']:
                reduced_data['gender'][value] += count
            else:
                reduced_data['gender'][value] = count
        elif group == 'nationality':
            if value in reduced_data['nationality']:
                reduced_data['nationality'][value] += count
            else:
                reduced_data['nationality'][value] = count

    return reduced_data

# Perform the MapReduce job
def map_reduce_customers():
    customers = Customer.objects.all()  # Get all customers
    mapped_data = map_customers(customers)  # Map step
    reduced_data = reduce_customers(mapped_data)  # Reduce step
    return reduced_data
