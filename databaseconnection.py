import pymysql
import json

class DBC:

    #Methods about actions before and after other methods

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = pymysql.connect(host='mysql-container',user="root", password='root', port=3306, database='TestingAPI')
            self.cursor = self.connection.cursor()
            return self
        
        except:
            print("There was a critical problem with the database connection")
            return
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    #Methods

    #To insert data
    def inserting_data(self, data):

        with self.cursor as cursor:

            my_query_inserting = "INSERT INTO Library (title, author) VALUES (%s, %s)"
            data_tuple = (data["title"],data["author"])

            try:
                cursor.execute(my_query_inserting, data_tuple)
            except:
                print("There was a problem on a data insertion!")

    #To select data
    def selecting_data(self):

        with self.cursor as cursor:

            my_query_select = "SELECT * FROM Library"

            try:
                cursor.execute(my_query_select)
                rows = cursor.fetchall()

                return rows
            except:
                print("There was a problem on a data selection!!")
                return

    #To select data with a serching clause
    def selecting_data_id(self, search):

        with self.cursor as cursor:
            
            my_query_select = f"SELECT * FROM Library WHERE ID = {search}"

            try:
                cursor.execute(my_query_select)
                rows = cursor.fetchall()

                return rows
            except:
                print(f"There was a problem on a data selection by the {search} id!!")
                return

    #To delete data
    def delete_data(self, search):

        with self.cursor as cursor:

            my_query_delete = f"DELETE FROM Library WHERE ID = {search}"

            try:
                cursor.execute(my_query_delete)
            except:
                print(f"There was a problem on a data deletion by the {search} id!!")
            
    #To update data
    def update_data(self, search, json_data):

        with self.cursor as cursor:

            my_query_update = "UPDATE Library SET title = %s, author = %s WHERE ID = %s"
            json_data_tuple = (json_data["title"], json_data["author"], search)
            
            try:
                cursor.execute(my_query_update, json_data_tuple)
            except:
                print(f"There was a problem on a data update by the {search} id!!")