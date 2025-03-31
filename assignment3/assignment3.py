# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
print("Task 1: Introduction to Pandas - Creating and Manipulating DataFrames")

import pandas as pd

# 1a. Create a DataFrame from a dictionary
task1_dict = {
    'Name': ['Alice', 'Bob', 'charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(task1_dict)
print(task1_data_frame)

# another way to create the DataFrame
# data_alice = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}
# data_bob = {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'}
# data_charlie = {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
# task1_data_frame = pd.DataFrame([data_alice, data_bob, data_charlie])
# print(task1_data_frame)

# 1b. Add a new column
task1_with_salary = task1_data_frame.copy()
salary = [70000, 80000, 90000]
task1_with_salary["Salary"] = salary
print(task1_with_salary)

# 1c. Modify an existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
print(task1_older)

# 1d. Save the DataFrame as a CSV file
task1_older.to_csv('employees.csv', index=False)
with open('employees.csv', 'r') as file:
    print(file.read())

# Task 2: Loading Data from CSV and JSON
print("Task 2: Loading Data from CSV and JSON")

# 2a. Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# 2b. Read data from a JSON file
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# 2c. Combine DataFrames
more_employees = pd.concat([task1_older, json_employees], ignore_index=True)
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
print("Task 3: Data Inspection - Using Head, Tail, and Info Methods")

# 3a. Use the head() method
first_three = more_employees.head(3)
print(first_three)

# 3b. Use the tail() method
last_two = more_employees.tail(2)
print(last_two)

# 3c. Get the shape of a DataFrame
employee_shape = more_employees.shape
print(employee_shape)

# 3d. Use the info() method
print(more_employees.info())

# Task 4: Data Cleaning
print("Task 4: Data Cleaning")

# 4a. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()
print(clean_data)

# 4b. Remove any duplicate rows from the DataFrame
clean_data.drop_duplicates(inplace=True)
print(clean_data)

# 4c. Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
mean_age = clean_data['Age'].mean()
clean_data['Age'].fillna(mean_age, inplace=True)
print(clean_data)

# 4d. Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print(clean_data)

# 4e. Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_age)
median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)
print(clean_data)

# 4f. Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print(clean_data)

# 4g. Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print(clean_data)