import sqlite3

# Connect to the database (create it if not exists)
conn = sqlite3.connect('products.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the products table
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL,
                    image_url TEXT,
                    categories TEXT
                )''')

# Sample data to populate the table
sample_data = [
    ("Hisense musice sounbar", 1.99, "data:image/png;base64,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", "Music"),
    ("Canon", 0.99, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq0A1LLYTiQK3Sd_FT41tPSkbsISdzjnaTDg&usqp=CAU", "Camera"),
    ("Macbook M1", 2.49, "data:image/jpeg;base64,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", "Laptops"),
    ("hisense Tv", 3.99, "data:image/jpeg;base64,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","TV"),
    ("Hp elitebook 4390", 4.49, "data:image/jpeg;base64,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","Laptops"),
]

# Insert sample data into the table
cursor.executemany('''INSERT INTO products (name, price, image_url,categories)
                        VALUES (?, ?, ?,?)''', sample_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
