# Task 2: Read a CSV File
print("Task 2: Read a CSV File")

import csv

def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            csv_reader = csv.reader(file)

            for i, row in enumerate(csv_reader):
                if i == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)

            employees_dict["rows"] = rows

    except Exception as e:
        print(f"An error has occurred: {e}")
        exit(1)

    return employees_dict

employees = read_employees()

print(employees)

# Task 3: Find the Column Index
print("Task 3: Find the Column Index")

def column_index(first_name):

    try:
        return employees["fields"].index(first_name)
    
    except ValueError:
        print(f"Column '{first_name}' not found.")
        return -1

employee_id_column = column_index("employee_id")

print(f"The index of 'employee_id' is: {employee_id_column}") 

# Task 4: Find the Employee First Name
print("Task 4: Find the Employee First Name")

def first_name(row_number):
    try:
        first_name_index = column_index("first_name")
        row = employees["rows"][row_number]
        return row[first_name_index]
    except Exception as e:
        print(f"An error occured: {e}")
        return None
    
# Task 5: Find the Employee: a Function in a Function
print("Task 5: Find the Employee: a Function in a Function")

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

matches = employee_find(1)

print(matches)

# Task 6: Find the Employee with a Lambda
print("Task 6: Find the Employee with a Lambda")
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

matches = employee_find_2(1)

print(matches)

# Task 7: Sort the Rows by last_name Using a Lambda
print("Task 7: Sort the Rows by last_name Using a Lambda")

last_name_column = column_index("last_name")

def sort_by_last_name():
    employees["rows"] = sorted(employees["rows"], key=lambda row: row[last_name_column])
    return employees["rows"]

print(sort_by_last_name())

# Task 8: Create a dict for an Employee
print("Task 8: Create a dict for an Employee")

def employee_dict(row):
    employee_data = zip(employees["fields"][1:], row[1:])
    return dict(employee_data)

print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, for All Employees
print("Task 9: A dict of dicts, for All Employees")

def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[0]
        employee_details = employee_dict(row)
        all_employees[employee_id] = employee_details
    
    return all_employees

print(all_employees_dict())

# Task 10: Use the os Module
print("Task 10: Use the os Module")

import os

def get_this_value():
    return os.getenv('THISVALUE')

print(get_this_value())

# Task 11: Creating Your Own Module
print("Task 11: Creating Your Own Module")

import custom_module

def set_that_secret(x):
    custom_module.set_secret(x)

set_that_secret("abracadabra!")

print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
print("Task 12: Read minutes1.csv and minutes2.csv")

import csv
import os

def read_csv(file_path):
    data = {'fields': [], 'rows': []}
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        data['fields'] = next(reader)
        for row in reader:
            data['rows'].append(tuple(row))
        return data

def read_minutes():
    v1 = read_csv('../csv/minutes1.csv')
    v2 = read_csv('../csv/minutes2.csv')
    return v1, v2

minutes1, minutes2 = read_minutes()

print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)

# Task 13: Create minutes_set
print("Task 13: Create minutes_set")

def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])

    combined_set = set1.union(set2)

    return combined_set

minutes_set = create_minutes_set()

print("Minutes set:", minutes_set)

# Task 14: Convert to datetime
print("Task 14: Convert to datetime")

from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)

    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    
    return converted_list

minutes_list = create_minutes_list()

print("Minutes list:", minutes_list)

#Task 15: Write Out Sorted List
print("Task 15: Write Out Sorted List")

import csv

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    return converted_list

    with open("minutes.csv", "w", newline="") as files:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerrows(converted_list)

print(write_sorted_list())