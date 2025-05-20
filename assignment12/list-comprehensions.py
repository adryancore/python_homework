import pandas as pd

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv("../csv/employees.csv")

# Step 2: Create a list of full names using a list comprehension
full_names = [row['first_name'] + " " + row['last_name'] for _, row in df.iterrows()]
print("All employee names:")
print(full_names)

# Step 3: Create a list of names that contain the letter 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nEmployee names containing the letter 'e':")
print(names_with_e)