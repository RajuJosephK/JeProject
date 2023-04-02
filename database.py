
# importing the database tool
import sqlite3

# class with every thing to do with the database
class database():
    # this initilies the objects attribures
    def __init__(self):
        pass
    # class to create connection with database
    def create_database(self, db_name):
        conn = sqlite3.connect(db_name)
        conn.close()

    # function to add, delete modify data in database
    # passing in the name of the database, quert and data 
    def execute_sql_query(self, db_name, sql_query, data):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        # executing the query
        result = cursor.execute(sql_query, data)
        conn.close()
        return result

    # specificaly so we can add data into the database
    def insert_data(self, db_name, sql_query, data):
        # creating the conection
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        # executing the query
        cursor.executemany(sql_query, data)
        conn.commit()
        conn.close()

    # specificaly so we can delet enteries
    def delete_data(self, db_name, sql_query):
        # creating connection to the database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        # executing the query
        cursor.execute(sql_query)
        conn.commit()
        conn.close()

 