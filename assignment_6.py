#!/usr/bin/env python
# coding: utf-8

# Here I create a sample data set

# Define some suppliers as dictionaries
first_supplier = {'city': 'Sydney',
    'contact_firstname': 'Robert',
    'contact_lastname': 'Mogabe',
    'contact_title': 'Mr',
    'country': 'Australia',
    'email': 'rob.mob@gmail.com',
    'notes': "dictator",
    'phone': '(03) 9323 7763',
    'postcode': 3000,
    'state': 'QLD',
    'street_address': 'Somewhere in Africa',
    'supplier_id': 53,
    'supplier_name': 'RobMog Ltd'}
second_supplier = {'city': 'Woking',
    'contact_firstname': 'Kenneth',
    'contact_lastname': 'Moresby',
    'contact_title': 'Mr',
    'country': 'Australia',
    'email': 'k.moresby@gmail.com',
    'notes': "",
    'phone': '(03) 9343 0665',
    'postcode': 3671,
    'state': 'QLD',
    'street_address': '3 The Green Walk',
    'supplier_id': 52,
    'supplier_name': 'KM Ltd'}
third_supplier = {'city': 'Sydney',
    'contact_firstname': 'Josh',
    'contact_lastname': 'Joshson',
    'contact_title': 'Mr',
    'country': 'Australia',
    'email': 'jjjjj@gmail.com',
    'notes': "",
    'phone': '(04) 1234 0665',
    'postcode': 2929,
    'state': 'NSW',
    'street_address': '4 Park Lane',
    'supplier_id': 50,
    'supplier_name': 'JJ&J Ltd'}

# Collate the dictionaries into a list called "suppliers"
suppliers = [first_supplier, second_supplier, third_supplier]


# # Coding Assignment 6
# 
# Course code/name:  
# Student name:  
# Student number:  

# ## A1

# Select an individual dictionary from suppliers & assign it as 'sup'
sup = suppliers[0].copy()

# Q1: Find keys of sup
sup_keys = list(suppliers[0].keys())
print('The keys of the dictionary "sup" are: {}'.format(sup_keys))

# Q2: Find the values of sup
sup_values = list(suppliers[0].values())
print('The values of the dictionary "sup" are: {}'.format(sup_values))

# Q3: Check for the key "mobile"
if 'mobile' in sup_keys:
    print('The key "mobile" exists in sup! :)')
else:
    print('The key "mobile" does not exist in sup :(')

# Q4: Delete all items from the dictionary "sup"
sup.clear()
# check that items are actually gone
num_items_in_sup = len(sup)
if num_items_in_sup == 0:
    print('"sup" now holds {} items and is therefore empty'.format(num_items_in_sup))
else:
    print('"sup" still holds {} items'.format(num_items_in_sup))


# ## A2

# Q1: Find the length of "suppliers"
length_suppliers = len(suppliers)
print('The list "suppliers" holds {} dictionaries'.format(length_suppliers))

# Q2: Change contact_firstname of supplier with supplier_id=52 from Kenneth to Ken
for supplier in suppliers:
    if supplier['supplier_id'] == 52:
        existing_name = supplier['contact_firstname']
        supplier['contact_firstname'] = 'Ken'
        print('Supplier name changed from "{}" to "Ken"'.format(existing_name))

# Q3: Add a new supplier to the list of suppliers
# define the new entry
new_supplier = {'city': 'Lancaster',
                'contact_firstname': 'Tracy',
                'contact_lastname': 'Wilson',
                'contact_title': 'Mrs',
                'country': 'Australia',
                'email': 'tracy4587.wilson@gmail.com',
                'notes': "",
                'phone': '(03) 9323 0663',
                'postcode': 3620,
                'state': 'VIC',
                'street_address': 'Suite 141/8 Black Dale',
                'supplier_id': 55,
                'supplier_name': 'Scott Ltd'}
# add the new entry to "suppliers"
suppliers.append(new_supplier)

# Q4: Remove supplier with supplier_id=53 from "suppliers"
for supplier in suppliers:
    if supplier['supplier_id'] == 53:
        suppliers.remove(supplier)
        print('Removed supplier with supplier_id=53')


# ## A3

# Define function that calculates requested properties of a list of numbers
def list_properties(numerical_list):

    print('The list {} has the following properties:'.format(numerical_list))

    # find the length of the list
    list_length = len(numerical_list)
    print('Length: {}'.format(list_length))

    # compute the sum of all items
    list_sum = sum(numerical_list)
    print('Sum: {}'.format(list_sum))

    # compute list average
    list_average = list_sum / list_length
    print('Average {}'.format(list_average))

    # find the minimum value of the list
    list_min = min(numerical_list)
    print('Minimum value: {}'.format(list_min))

    return list_length, list_sum, list_average, list_min

# Define the requested list
sample_list = [1, 55, 10, 20, 30]

# Save list properties for "sample_list"
sample_length, sample_sum, sample_average, sample_min = list_properties(sample_list)


# ## A4

# Q1: Process the list of dictionaries to create a list of supplier names
supplier_names = []
for supplier in suppliers:
    supplier_names.append(supplier['supplier_name'])
print('Supplier names: {}'.format(supplier_names))

# Q2: Join the supplier_name with a semi-colon followed by space to form a single string and print the string
names_as_string = '; '.join(supplier_names)
print('Supplier names as a string: {}'.format(names_as_string))


# ## A5

# Q1: Create the dictionary prod_155
prod_155 = {'discontinued': 0,
            'lead_time_days': 3,
            'product_category': 'Wireless Phone',
            'product_description': 'Display: 5.1-inches Camera: ...',
            'product_id': 155,
            'product_name': 'Samsung Galaxy S5, Black 16GB (Sprint)',
            'reorder_level': 18,
            'unit_price': 699.99}

# Q2: Print prod_155
print(prod_155)


# ## A6

# Q1: Process the list of dictionaries to create a new list of dictionaries with only suppliers from "VIC" or "NSW"
new_suppliers = list(filter(lambda d: d['state'] in ['VIC', 'NSW'], suppliers))

# Q2: Print the length of the new list
new_suppliers_length = len(new_suppliers)
print('The new list has length {}'.format(new_suppliers_length))

# Q3: Print the contents of the new list
print('The new suppliers list is:')
print(new_suppliers)


# ## A7

# Q1: Process the list of dictionaries to create a list of supplier names formatted as city: supplier_id, supplier_name
supplier_names_special_format = list(map(lambda x: '{}: {}, {}'.format(x['city'], x['supplier_id'], x['supplier_name']), suppliers))

# Q2: Print the newly created list
print(supplier_names_special_format)


# ## A8

# Q1: Convert the Australian date string 02/03/2022 to a python date object
import datetime
date_object = datetime.datetime.strptime('02/03/2022', "%d/%m/%Y").date()

# Q2: Print the date object without any formatting\
print('Printed date object for 02/03/2022:')
print(date_object)

# Create a date object for the Australian date 28/02/2022 and print the date object in Australian format
new_obj = datetime.datetime.strptime('28/02/2022', "%d/%m/%Y").date()
print('Printed date object for 28/02/2022 in Australian format:')
print(new_obj.strftime("%d/%m/%Y"))


# ## A9

# Write a program to print the area code of an Australian land line phone number (given as a string)
import re

def print_area_code(phone_number):

    # find the area code
    area_code = re.compile("\((.*)\)").search(phone_number).group(1)

    # print the area code
    print('The area code for the number {} is: {}'.format(phone_number, area_code))


# ## A10

# Q1: Write Python code to implement a class to represent a Supplier as per the given specifications

class Supplier:

    # Initialize the class using a dict 
    def __init__(self, supplier):
        
        self.city = supplier['city']
        self.contact_firstname = supplier['contact_firstname']
        self.contact_lastname = supplier['contact_lastname']
        self.contact_title = supplier['contact_title']
        self.country = supplier['country']
        self.email = supplier['email']
        self.notes = supplier['notes']
        self.phone = supplier['phone']
        self.postcode = supplier['postcode']
        self.state = supplier['state']
        self.street_address = supplier['street_address']
        self.supplier_id = supplier['supplier_id']
        self.supplier_name = supplier['supplier_name']

    # Define a function to set / re-set the instance attribute "phone"
    def set_phone(self, phone_number):
        self.phone = phone_number

    # Define a function to retrieve the instance attribute "phone"
    def get_phone(self):
        print(self.phone)

# Q2: Test the class and its methods to show that it works
supp = Supplier(suppliers[2])
supp.set_phone('(03) 9961 5555')
supp.get_phone()




