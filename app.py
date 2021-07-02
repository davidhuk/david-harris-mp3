import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("home_page.html")


@app.route("/alcoholic_cocktails")
def alcoholic_cocktails():
    alcoholic_cocktails = list(mongo.db.alcoholic_cocktails.find())
    return render_template("alcoholic_cocktails.html",
                           alcoholic_cocktails=alcoholic_cocktails)


@app.route("/non_alcoholic_cocktails")
def non_alcoholic_cocktails():
    non_alcoholic_cocktails = list(mongo.db.non_alcoholic_cocktails.find())
    return render_template("non_alcoholic_cocktails.html",
                           non_alcoholic_cocktails=non_alcoholic_cocktails)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        # checks database to see if user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # creates flash error for user notification
        if existing_user:
            flash("ERROR: Username already in use.")
            return redirect(url_for("register_user"))

        # posts user data to the database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
    return render_template("register_user.html")


@app.route("/user_profile")
def user_profile():
    return render_template("user_profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP")),
    port = int(os.environ.get("PORT"))
