import sqlite3

def fetch_order_totals():
    # Connect to the SQLite database
    conn = sqlite3.connect('/path/to/your/database.db')
    cursor = conn.cursor()

    # Define the SQL query
    query = '''
    SELECT o.order_id, 
           SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    '''

    # Execute the query
    cursor.execute(query)

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(f"Order ID: {row[0]}, Total Price: ${row[1]:.2f}")

    # Close the connection
    conn.close()

if __name__ == '__main__':
    fetch_order_totals()