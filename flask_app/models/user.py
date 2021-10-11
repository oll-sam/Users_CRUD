from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self,data):
        self.idusers = data["idusers"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updates_at = data["updates_at"]

    @classmethod
    def insert_user(cls,data):
        query =  "INSERT INTO users (first_name, last_name, email, created_at, updates_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"
        return connectToMySQL ("mydb").query_db(query,data)

    @classmethod
    def get_all_users(cls):
        query ="SELECT * FROM users ORDER BY idusers DESC"
        mydb = connectToMySQL ("mydb").query_db(query)
        users = []

        for u in mydb:
            users.append(cls(u))
        
        return users

    @classmethod
    def select_users(cls,data):
        query ="SELECT * FROM users WHERE idusers = %(idusers)s"
        mydb = connectToMySQL ("mydb").query_db(query,data)
        user = []

        return cls(mydb[0])

    @classmethod
    def get_users(cls,data):
        query ="SELECT * FROM users WHERE idusers = %(idusers)s"
        mydb = connectToMySQL ("mydb").query_db(query,data)
        user = []

        return cls(mydb[0])

    @classmethod
    def update_user(cls,data):
        query =  "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE idusers = %(idusers)s"
        return connectToMySQL ("mydb").query_db(query,data)

    @classmethod
    def delete_users(cls,data):
        query = "DELETE FROM users WHERE idusers = %(idusers)s"
        return connectToMySQL ("mydb").query_db(query,data)