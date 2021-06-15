import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRECT_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_alcoholic_cocktails")
def get_alcoholic_cocktails():
    alcoholic_cocktails = list(mongo.db.alcoholic_cocktails.find())
    return render_template(
        "alcoholic_cocktails.html",
        alcoholic_cocktails=alcoholic_cocktails)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP")),
    port = int(os.environ.get("PORT")),
    debug = True
