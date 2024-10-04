import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_devices():
    conn = get_db_connection()
    devices = conn.execute('SELECT * FROM devices').fetchall()
    conn.close()
    return devices

def update_device_price(device_id, new_price):
    conn = get_db_connection()
    conn.execute('UPDATE devices SET price = ? WHERE id = ?', (new_price, device_id))
    conn.commit()
    conn.close()

def create_user(username, password):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def check_user_credentials(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    conn.close()
    return user is not None

def add_device_submission(username, brand, model):
    conn = get_db_connection()
    conn.execute('INSERT INTO device_submissions (username, brand, model) VALUES (?, ?, ?)', (username, brand, model))
    conn.commit()
    conn.close()