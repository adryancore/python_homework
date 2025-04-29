import sqlite3
import pandas as pd

# Create and connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Step 1: Create required tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS line_items (
    line_item_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);
""")

# Step 2: Insert sample data into products and line_items tables

# Insert products
cursor.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", ('Product A', 10.0))
cursor.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", ('Product B', 20.0))
cursor.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", ('Product C', 30.0))

# Insert line_items
cursor.execute("INSERT INTO line_items (product_id, quantity) VALUES (?, ?)", (1, 5))  # 5 of Product A
cursor.execute("INSERT INTO line_items (product_id, quantity) VALUES (?, ?)", (2, 3))  # 3 of Product B
cursor.execute("INSERT INTO line_items (product_id, quantity) VALUES (?, ?)", (3, 2))  # 2 of Product C

# Commit the changes to the database
conn.commit()

# Step 3: Read data into a DataFrame with JOIN
query = """
SELECT line_items.line_item_id, line_items.quantity, line_items.product_id,
       products.product_name, products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id;
"""

df = pd.read_sql_query(query, conn)

# Step 4: Print first 5 rows of the DataFrame
print("Initial DataFrame:")
print(df.head())

# Step 5: Add a 'total' column (quantity * price)
df['total'] = df['quantity'] * df['price']

# Step 6: Print first 5 rows again after adding the 'total' column
print("\nDataFrame with 'total' column:")
print(df.head())

# Step 7: Group by product_id
summary = df.groupby('product_id').agg({
    'line_item_id': 'count', 
    'total': 'sum', 
    'product_name': 'first'
})

# Step 8: Print the summary DataFrame
print("\nGrouped and Aggregated DataFrame:")
print(summary.head())

# Step 9: Sort by product_name
summary = summary.sort_values('product_name')

# Step 10: Write the summary DataFrame to a CSV file
summary.to_csv("order_summary.csv")

# Close the connection
conn.close()

# Reconnect to check the tables in the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Get all the table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("\nTables in database:", tables)

conn.close()
