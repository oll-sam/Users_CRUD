from flask import Flask, render_template , request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all_users()
    return render_template("index.html", users=users)

@app.route("/users/new", methods=["POST"])
def new():
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


if __name__ == "__main__":
    app.run(debug=True)