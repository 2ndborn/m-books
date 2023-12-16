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
@app.route("/get_titles")
def get_titles():
    titles = list(mongo.db.titles.find())
    return render_template("titles.html", titles=titles)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # The new user is placed into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check to see if the username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure the hashed password matches users input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Greetings! {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # incorrect password entered
                flash("Incorrect Username and/or Password entered")
                return redirect(url_for("signin"))

        else:
            # username doesn't existing
            flash("Incorrect Username and/or Password entered")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # locate user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("signin"))


@app.route("/signout")
def signout():
    # remove cookies from the user
    flash("You have signed out")
    session.pop("user")
    return redirect("signin")


@app.route("/summary/<titles_id>")
def summary(titles_id):
    titles = list(mongo.db.titles.find({"_id": ObjectId(titles_id)}))
    reviews = list(mongo.db.reviews.find())
    return render_template("summary.html", titles=titles, reviews=reviews)


@app.route("/add_title", methods=["GET", "POST"])
def add_title():
    if request.method == "POST":
        title = {
            "title_name": request.form.get("title_name"),
            "title_year": request.form.get("title_year"),
            "title_chapters": request.form.get("title_chapters"),
            "title_mangaka": request.form.get("title_mangaka"),
            "title_story": request.form.get("title_story"),
            "title_image": request.form.get("title_image"),
            "title_rname": request.form.get("title_rname"),
            "title_review": request.form.get("title_review"),
            "created_by": session["user"]
        }
        mongo.db.titles.insert_one(title)
        flash("Title Successfully Added")
        return redirect(url_for("get_titles"))

    return render_template("add_title.html")


@app.route("/edit_title/<title_id>", methods=["GET", "POST"])
def edit_title(title_id):
    if request.method == "POST":
        submit = {
            "title_name": request.form.get("title_name"),
            "title_year": request.form.get("title_year"),
            "title_chapters": request.form.get("title_chapters"),
            "title_mangaka": request.form.get("title_mangaka"),
            "title_story": request.form.get("title_story"),
            "title_image": request.form.get("title_image"),
            "created_by": session["user"]
        }
        mongo.db.titles.update_many(
            {"_id": ObjectId(title_id)}, {"$set": submit})
        flash("Title Successfully Updated")
        return redirect(url_for("get_titles"))

    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    return render_template("summary.html", title=title)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "review_header": request.form.get("review_header"),
            "review_name": request.form.get("review_name"),
            "review_review": request.form.get("review_review"),
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_titles"))


@app.route("/show_review", methods=["GET", "POST"])
def show_review():
    # Assuming you have a MongoDB connection named 'mongo'
    titles_collection = mongo.db.titles
    reviews_collection = mongo.db.reviews

    # Fetch specific fields from the documents
    title_name = titles_collection.find_one()["title_name"]
    review_header = reviews_collection.find_one()["review_header"]

    if title_name == review_header:
        print("review_name", "review_review")


@app.route("/delete_title/<title_id>")
def delete_title(title_id):
    mongo.db.titles.delete_one({"_id": ObjectId(title_id)})
    flash("Title Successfully Deleted")
    return redirect(url_for("get_titles"))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Title Successfully Deleted")
    return redirect(url_for("get_titles"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
