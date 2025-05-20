import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# Step 2: SQL to get total price per order
query = """
SELECT o.order_id, 
       SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# Step 3: Load into DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Calculate cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

# Optional: close the connection
conn.close()

# Step 5: Plot cumulative revenue
df.plot(
    x="order_id", 
    y="cumulative", 
    kind="line", 
    color="green", 
    marker='o', 
    title="Cumulative Revenue by Order"
)

plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()