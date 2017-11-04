# What is a Context Manager?

# It is a handy construct that enables us to set something up
# and tear something down automatically

# Open a file, write a bunch of stuff to it, then close it
# Python creates one automatically for you when you use the with statement

# The way it works under the hood is by using Pythons magic methods
# - __enter__
# - __exit__

# EXAMPLE
#------------

import sqlite3

class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise

if __name__ == "__main__":
    db = 'test.db'
    with DataConn(db) as conn:
        cursor = conn.cursor()

# The __enter__ method executes automatically
# The Context Manager created by the with statement will call the DataConn
# classes __enter__ and __exit__ methods
