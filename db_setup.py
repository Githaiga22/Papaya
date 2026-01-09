"""
 * @title Papaya Database Setup
 * @author Allan Robinson
 * @notice Database initialization and table creation for Papaya
 * @dev Created: January 9, 2026
 * Tables: users, user_assets, borrowed_assets, interest_rates, liquidations, transactions
 """

import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('mydb.db') # create a persistent database
        return conn
    except Error as e:
        print(e)

def create_tables():
    conn = create_connection()
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS interest_rates
                          (asset text, interest_rate real, timestamp datetime default current_timestamp)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (_id text primary key, username text, password text)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS user_assets
                     (user_id text, asset text, balance integer, timestamp datetime default current_timestamp,
                      FOREIGN KEY(user_id) REFERENCES users(_id))''')
        conn.execute('''CREATE TABLE IF NOT EXISTS borrowed_assets
                     (user_id text, asset text, amount integer, timestamp datetime default current_timestamp,
                      FOREIGN KEY(user_id) REFERENCES users(_id))''')
        conn.execute('''CREATE TABLE IF NOT EXISTS liquidations
                    (user_id text, asset text, amount integer, date datetime default current_timestamp)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     user_id text,
                     tx_type text,
                     asset text,
                     amount real,
                     from_asset text,
                     to_asset text,
                     tx_hash text,
                     status text,
                     timestamp datetime default current_timestamp,
                     FOREIGN KEY(user_id) REFERENCES users(_id))''')
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
