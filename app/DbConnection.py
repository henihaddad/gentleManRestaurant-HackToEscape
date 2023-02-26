import sqlite3


class DbConnection:
    def __init__(self):
        self.sql_connect = sqlite3.connect('database.db')

    def exec_query(self, query):
        cursor = self.sql_connect.cursor()
        results = cursor.execute(query).fetchall()
        self.sql_connect.commit()
        return results
