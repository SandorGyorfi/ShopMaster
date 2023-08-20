import os
from decouple import config

from bson.objectid import ObjectId
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mail import Mail, Message
from datetime import datetime


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return redirect(url_for("main_page"))


@app.route("/main_page")
def main_page():
    return render_template("main_page.html")


@app.route("/get_items")
def get_items():
    if not session.get("user"):
        return redirect(url_for("login"))

    user_items = list(mongo.db.item.find({"created_by": session["user"]}))
    return render_template("items.html", items=user_items)


@app.route("/search", methods=["GET", "POST"])
def search():
    if not session.get("user"):
        return redirect(url_for("login"))

    query = request.form.get("query")
    user_items = list(
        mongo.db.item.find({"created_by": session["user"], "$text": {"$search": query}})
    )
    return render_template("items.html", items=user_items)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")}
        )

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Passwords do not match", "error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(password),
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username")
        flash("Registration Successful!", "success")
        return redirect(url_for("profile", username=session["user"]))

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
                return redirect(
                    url_for("profile", username=session["user"])
                )  # Redirect to profile
            else:
                flash("Invalid login details")
                return redirect(url_for("login"))

        else:
            flash("Invalid login details")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/change_email", methods=["GET", "POST"])
def change_email():
    """
    Handle the change email form submission.

    This function allows a user to change their email address.

    Returns:
        Redirect: Redirects to the user's profile page.
    """
    if session.get("user"):
        if request.method == "POST":
            new_email = request.form.get("new_email")
            password = request.form.get("password")

            user = mongo.db.users.find_one({"username": session["user"]})
            if user and check_password_hash(user["password"], password):
                mongo.db.users.update_one(
                    {"username": session["user"]}, {"$set": {"email": new_email}}
                )
                flash("Email address changed successfully!", "success")
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Invalid password", "error")
                return redirect(url_for("change_email"))

        return render_template("change_email.html", username=session["user"])
    return redirect(url_for("login"))


@app.route("/renew_username", methods=["GET", "POST"])
def renew_username():
    """
    Handle the renew username form submission.

    This function allows a user to renew their username.

    Returns:
        Redirect: Redirects to the user's profile page with the updated username.
    """
    if session.get("user"):
        if request.method == "POST":
            new_username = request.form.get("new_username")

            existing_user = mongo.db.users.find_one({"username": new_username})
            if existing_user:
                flash("Username already exists", "error")
                return redirect(url_for("renew_username"))

            mongo.db.users.update_one(
                {"username": session["user"]}, {"$set": {"username": new_username}}
            )
            session["user"] = new_username
            flash("Username renewed successfully!", "success")
            return redirect(url_for("profile", username=new_username))

        return render_template("renew_username.html", username=session["user"])
    return redirect(url_for("login"))


@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    if session.get("user"):
        if request.method == "POST":
            current_password = request.form.get("current_password")
            new_password = request.form.get("new_password")
            confirm_password = request.form.get("confirm_password")

            user = mongo.db.users.find_one({"username": session["user"]})
            if user and check_password_hash(user["password"], current_password):
                if new_password == confirm_password:
                    new_password_hash = generate_password_hash(new_password)
                    mongo.db.users.update_one(
                        {"username": session["user"]},
                        {"$set": {"password": new_password_hash}},
                    )
                    flash("Password changed successfully!", "success")
                    return redirect(url_for("profile", username=session["user"]))
                else:
                    flash("Passwords do not match", "error")
            else:
                flash("Invalid password", "error")

        return render_template("change_password.html", username=session["user"])
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))


@app.route("/delete_account")
def delete_account():
    if session.get("user"):
        mongo.db.users.delete_one({"username": session["user"]})
        flash("Account deleted successfully!", "success")
        session.pop("user")
    return redirect(url_for("login"))


@app.route("/delete_account_confirm")
def delete_account_confirm():
    if session.get("user"):
        return render_template("delete_account_confirm.html")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    """
    Handle the add item form submission.

    This function allows a user to add a new item to their list.

    Returns:
        Redirect: Redirects to the user's list of items after adding a new item.
    """
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
    """
    Handle the edit item form submission.

    This function allows a user to edit an existing item on their list.

    Args:
        item_id (str): The ID of the item to be edited.

    Returns:
        Redirect: Redirects to the user's list of items after editing an item.
    """
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "item_name": request.form.get("item_name"),
            "comment": request.form.get("comment"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
        }
        mongo.db.item.update({"_id": ObjectId(item_id)}, submit)
        flash("Item updated successfully!", "success")
        return redirect(url_for("get_items"))

    item = mongo.db.item.find_one({"_id": ObjectId(item_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_item.html", item=item, categories=categories)


@app.route("/delete_item/<item_id>", methods=["GET", "POST"])
def delete_item(item_id):
    mongo.db.item.remove({"_id": ObjectId(item_id)})
    flash("Item deleted successfully!", "success")
    return redirect(url_for("get_items"))


@app.route("/get_categories")
def get_categories():
    """
    Retrieve and render a list of categories.

    This function retrieves a list of categories

      from the database and renders them on the categories page.

    Returns:
        Rendered template: Renders the "categories.html"

        template with the list of categories.
    """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Handle the addition of a new category.

    This function allows users to add a new category to the database.

    Returns:
        Redirect: Redirects to the "get_categories"

        route after adding a category.
    """
    if request.method == "POST":
        category = {"category_name": request.form.get("category_name")}
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Handle the editing of a category.

    This function allows users to edit

    the name of an existing category in the database.

    Args:
        category_id (str): The ID of the category to be edited.

    Returns:
        Redirect: Redirects to the "get_categories"

           route after editing a category.
    """
    if request.method == "POST":
        submit = {"category_name": request.form.get("category_name")}
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category updated successfully!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Handle the deletion of a category.

    This function deletes a category based on the given category ID.

    Args:
        category_id (str): The ID of the category to be deleted.

    Returns:
        Redirect: Redirects to the categories

           page after deleting the category.
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category deleted successfully!")
    return redirect(url_for("get_categories"))


@app.route("/contact_developer", methods=["GET", "POST"])
def contact_developer():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        whatsapp_number = "+447563713196"
        click_to_chat_link = (
            f"https://wa.me/{whatsapp_number}?text=Name%3A%20{name}%0A"
            f"Email%3A%20{email}%0AMessage%3A%20{message}"
        )

        return redirect(click_to_chat_link)
    return render_template("contact_developer.html", username=session["user"])


@app.route("/handle_profile_action", methods=["POST"])
def handle_profile_action():
    """
    Handle profile action selection.

    This function handles the user's selection of a

       profile action, such as changing email or password.

    Returns:
        Redirect: Redirects to the selected action's URL.
    """
    selected_action = request.form.get("profile_action")
    return redirect(selected_action)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
