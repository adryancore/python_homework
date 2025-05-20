import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# Step 2: SQL query to get employee revenue
query = """
SELECT last_name, 
       SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

# Step 3: Load data into DataFrame
employee_results = pd.read_sql_query(query, conn)

# Step 4: Plot the results
employee_results.plot(
    x="last_name", 
    y="revenue", 
    kind="bar", 
    color="skyblue", 
    legend=False
)

plt.title("Revenue by Employee")
plt.xlabel("Employee Last Name")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 5: Close the connection
conn.close()