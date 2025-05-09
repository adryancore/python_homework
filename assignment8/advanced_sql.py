import sqlite3

def employees_with_many_orders():
    conn = sqlite3.connect('../db/lesson.db')
    cursor = conn.cursor()

    try:
        query = '''
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5
        ORDER BY order_count DESC;
        '''

        cursor.execute(query)
        results = cursor.fetchall()

        print("Employees with more than 5 orders:")
        for row in results:
            print(f"Employee ID: {row[0]}, Name: {row[1]} {row[2]}, Order Count: {row[3]}")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        conn.close()

if __name__ == '__main__':
    employees_with_many_orders()

