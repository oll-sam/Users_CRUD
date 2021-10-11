from flask import Flask, render_template , request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all_users()
    return render_template("index.html", users=users)

@app.route("/users/new", methods=["POST"])
def insert():
    data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
    }
    User.insert_user(data)
    return redirect("/users")

@app.route("/users")
def users():
    users = User.get_all_users()
    return render_template("create.html", users=users)

@app.route("/select/<int:idusers>")
def select(idusers):
    data = {
        "idusers": idusers
    }
    user = User.select_users(data)
    return render_template("select.html", user=user)

@app.route("/edit/<int:idusers>")
def edit(idusers):
    data = {
        "idusers": idusers
    }
    user = User.get_users(data)
    return render_template("edit_user.html", user=user)

@app.route("/edituser/<int:idusers>", methods=["POST"])
def update(idusers):
    data = {
            "idusers" : idusers,
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
    }
    User.update_user(data)
    return redirect("/users")

@app.route("/delete/<int:idusers>")
def delete(idusers):
    data = {
        "idusers": idusers
    }
    User.delete_users(data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)