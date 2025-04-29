# Task 1: Create a New SQLite Database

import sqlite3

with  sqlite3.connect("../db/magazines.db") as conn:
    print("Database created and connected successfully!")

# Task 2: Define Database Structure

    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = 1")

    # Create the publishers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    """)

    # Create the magazines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES publishers(id) ON DELETE CASCADE
    );
    """)

    # Create the subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    );
    """)

    # Create the subscriptions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
    );
    """)
    
    conn.commit()
print("Sample data inserted successfully!")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Task 3: Populate Tables with Data

# Task 3: Populate Tables with Data

    def add_publisher(cursor, name):
        try:
            cursor.execute("SELECT COUNT(*) FROM publishers WHERE name = ?", (name,))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Publisher '{name}' already exists!")
                return

            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
            print(f"Publisher '{name}' added successfully!")

        except sqlite3.Error as e:
            print("Error:", e)

    def add_magazine(cursor, title, publisher_id):
        try:
            cursor.execute("SELECT COUNT(*) FROM magazines WHERE title = ?", (title,))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Magazine '{title}' already exists!")
                return

            cursor.execute("INSERT INTO magazines (title, publisher_id) VALUES (?, ?)", (title, publisher_id))
            print(f"Magazine '{title}' added successfully!")

        except sqlite3.Error as e:
            print("Error:", e)

    def add_subscriber(cursor, name, address):
        try:
            cursor.execute("SELECT COUNT(*) FROM subscribers WHERE name = ? AND address = ?", (name, address))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Subscriber '{name}' with address '{address}' already exists!")
                return

            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
            print(f"Subscriber '{name}' added successfully!")

        except sqlite3.Error as e:
            print("Error:", e)

    def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
        try:
            cursor.execute("SELECT COUNT(*) FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Subscription for subscriber ID '{subscriber_id}' and magazine ID '{magazine_id}' already exists!")
                return

            cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                           (subscriber_id, magazine_id, expiration_date))
            print(f"Subscription added successfully!")

        except sqlite3.Error as e:
            print("Error:", e)

    # Populating the tables with at least 3 entries
    add_publisher(cursor, "Publisher One")
    add_publisher(cursor, "Publisher Two")
    add_publisher(cursor, "Publisher Three")

    add_magazine(cursor, "Magazine One", 1)  # Assume publisher_id 1
    add_magazine(cursor, "Magazine Two", 2)  # Assume publisher_id 2
    add_magazine(cursor, "Magazine Three", 3)  # Assume publisher_id 3

    add_subscriber(cursor, "Alice", "123 Main St")
    add_subscriber(cursor, "Bob", "456 Oak St")
    add_subscriber(cursor, "Charlie", "789 Pine St")

    add_subscription(cursor, 1, 1, "2025-12-31")  # subscriber_id 1, magazine_id 1
    add_subscription(cursor, 2, 2, "2025-11-30")  # subscriber_id 2, magazine_id 2
    add_subscription(cursor, 3, 3, "2025-10-15")  # subscriber_id 3, magazine_id 3

    conn.commit()

    print("Sample data inserted successfully!")

# Task 4: Write SQL Queries


# 1. Get all publishers
cursor.execute("SELECT * FROM publishers;")
publishers = cursor.fetchall()
print("Publishers:")
for publisher in publishers:
    print(publisher)

# 2. Get all magazines
cursor.execute("SELECT * FROM magazines;")
magazines = cursor.fetchall()
print("\nMagazines:")
for magazine in magazines:
    print(magazine)

# 3. Get all subscribers
cursor.execute("SELECT * FROM subscribers;")
subscribers = cursor.fetchall()
print("\nSubscribers:")
for subscriber in subscribers:
    print(subscriber)

# 4. Get all subscriptions
cursor.execute("SELECT * FROM subscriptions;")
subscriptions = cursor.fetchall()
print("\nSubscriptions:")
for subscription in subscriptions:
    print(subscription)

# 5. Get subscribers with their subscribed magazines (JOIN query)
cursor.execute("""
SELECT subscribers.name, magazines.title, subscriptions.expiration_date
FROM subscriptions
JOIN subscribers ON subscriptions.subscriber_id = subscribers.id
JOIN magazines ON subscriptions.magazine_id = magazines.id;
""")
subscription_info = cursor.fetchall()
print("\nSubscriber Magazine Subscriptions:")
for info in subscription_info:
    print(info)

# 6. Get subscribers who are subscribed to a specific magazine (e.g., "Magazine A")
cursor.execute("""
SELECT subscribers.name
FROM subscriptions
JOIN subscribers ON subscriptions.subscriber_id = subscribers.id
JOIN magazines ON subscriptions.magazine_id = magazines.id
WHERE magazines.title = ?;
""", ('Magazine A',))
subscribers_for_magazine = cursor.fetchall()
print("\nSubscribers for 'Magazine A':")
for subscriber in subscribers_for_magazine:
    print(subscriber)