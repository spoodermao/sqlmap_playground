import sqlite3
import os
import time

class DB:
    def __init__(self, db_dir):
        self.db = os.path.join(db_dir, "db.sqlite3")
        self.column_names = [
            "username",
            "password",
            "secret"
        ]

        self.init_db()

    def execute_query(self, query):
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute(query)
        result = curs.fetchall()
        conn.commit()
        conn.close()

        return result

    def init_db(self):
        if not os.path.exists(self.db):
            query = [
                """
                CREATE TABLE products (
                        prod TEXT PRIMARY KEY,
                        price TEXT,
                        count TEXT
                    );
                """,
                """
                CREATE TABLE login (
                        username TEXT PRIMARY KEY,
                        password TEXT,
                        secret TEXT
                    );
                """,
                """
                INSERT INTO login(username, password, secret) VALUES('admin', 'hardpasswordforadmin', 'adminsecret');
                """,
                """
                INSERT INTO login(username, password, secret) VALUES('user', 'simplepasswordforuser', 'usersecret');
                """,
                """
                Insert INTO products(prod, price, count) VALUES('apple', '10', '100');
                """,
                """
                Insert INTO products(prod, price, count) VALUES('banana', '20', '200');
                """,
                """
                Insert INTO products(prod, price, count) VALUES('orange', '30', '300');  
                """
            ]
            [self.execute_query(i) for i in query]
        

    def get(self, prod):
        rows = self.execute_query(f"SELECT *  FROM products WHERE prod = '{prod}'")
        if len(rows) != 0:
            return rows
        else:
            return None