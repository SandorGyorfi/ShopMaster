import os

from bson.objectid import ObjectId
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)



@app.route("/")
def index():
    return redirect(url_for("get_items"))


@app.route("/get_items")
def get_items():
    items = list(mongo.db.item.find())
    return render_template("items.html", items=items)




@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")}
        )

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username")
        flash("Registration Successful!", "success")

    return render_template("register.html")




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")}
        )

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(request.form.get("username")))
            else:
                flash("Invalid login details")
                return redirect(url_for("login"))

        else:
            flash("Invalid login details")
            return redirect(url_for("login"))

    return render_template("login.html")




@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))



@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        item = {
            "category_name": request.form.get("category_name"),
            "item_name": request.form.get("item_name"),
            "comment": request.form.get("comment"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
        }
        mongo.db.item.insert_one(item)
        flash("Item added successfully!", "success")
        return redirect(url_for("get_items"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_item.html", categories=categories)


@app.route("/edit_item/<item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = mongo.db.item.find_one({"_id": ObjectId(item_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_item.html", item=item, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
