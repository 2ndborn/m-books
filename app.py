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
# Retrieve the titles from the mongodb database
def get_titles():
    titles = list(mongo.db.titles.find().sort("title_name", 1))
    return render_template("titles.html", titles=titles)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    titles = list(mongo.db.titles.find({"$text": {"$search": query}}))
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
                flash("Welcome {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # incorrect password entered
                flash("Incorrect Username and/or Password entered")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password entered")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # locates user's username from database
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
    # retrieve the titles and reviews from the database
    titles = list(mongo.db.titles.find({"_id": ObjectId(titles_id)}))
    reviews = list(mongo.db.reviews.find({"title_id": ObjectId(titles_id)}))
    return render_template("summary.html", titles=titles, reviews=reviews)


@app.route("/add_title", methods=["GET", "POST"])
def add_title():
    # check if the user has logged in
    if not ('user' in session):
        return render_template("404.html")
    if request.method == "POST":
        # Check if the title already exists in the database
        title_name = request.form.get("title_name")
        if mongo.db.titles.find_one({"title_name": title_name}):
            flash("Title already exists")
        else:
            title = {
                "title_name": title_name,
                "title_year": request.form.get("title_year"),
                "title_status": request.form.get("title_status"),
                "title_mangaka": request.form.get("title_mangaka"),
                "title_story": request.form.get("title_story"),
                "title_image": request.form.get("title_image"),
                "title_rname": request.form.get("title_rname"),
                "title_review": request.form.get("title_review"),
                "created_by": session["user"]
            }
            # Inserts title variable into the database
            mongo.db.titles.insert_one(title)
            flash("Title Successfully Added")
            return redirect(url_for("get_titles"))

    return render_template("add_title.html")


@app.route("/add_review/<title_id>", methods=["GET", "POST"])
def add_review(title_id):
    # check if the user has logged in
    if not ('user' in session):
        return render_template("404.html")
    if request.method == "POST":
        # check if the user has reviewed title before
        username = mongo.db.users.find_one({"username": session["user"]})
        creator = (mongo.db.reviews.find_one(
            {"created_by": session["user"], "title_id": ObjectId(title_id)}))
        if creator is not None:
            # ensures user can review title again after review has been deleted
            flash("You have already reviewed this title.")
            return redirect(url_for("get_titles", title_id=title_id))
        else:
            review = {
                "review_name": request.form.get("review_name"),
                "review_review": request.form.get("review_review"),
                "created_by": session["user"],
                "title_id": ObjectId(title_id)
            }
            mongo.db.reviews.insert_one(review)
            flash("Review Successfully Added")
        return redirect(url_for("get_titles", title_id=title_id))


@app.route("/edit_title/<title_id>", methods=["GET", "POST"])
def edit_title(title_id):
    # check if the user has logged in
    if not ('user' in session):
        return render_template("404.html")
    if request.method == "POST":
        creator = mongo.db.titles.find_one(
            {"created_by": session["user"], "_id": title_id})
        admin = mongo.db.users.find_one({"username": "admin"})
        # if creator submits and update
        if creator or admin:
            submit = {
                "title_name": request.form.get("title_name"),
                "title_year": request.form.get("title_year"),
                "title_status": request.form.get("title_status"),
                "title_mangaka": request.form.get("title_mangaka"),
                "title_story": request.form.get("title_story"),
                "title_image": request.form.get("title_image"),
            }
            mongo.db.titles.update_many(
                {"_id": ObjectId(title_id)}, {"$set": submit})
            flash("Title Successfully Updated")
        else:
            # don't update if not the creator
            flash("Cannot be edited")
        return redirect(url_for("summary", titles_id=title_id))

    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    return render_template("summary.html", title=title)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # check if the user has logged in
    if not ('user' in session):
        return render_template("404.html")
    if request.method == "POST":
        creator = mongo.db.reviews.find_one(
            {"created_by": session["user"], "_id": review_id})
        admin = mongo.db.users.find_one({"username": "admin"})
        # ensures only the creator can edit the review
        if creator or admin:
            submit = {
                "review_name": request.form.get("review_name"),
                "review_review": request.form.get("review_review")
            }
            mongo.db.reviews.update_many(
                {"_id": ObjectId(review_id)}, {"$set": submit})
            flash("Review Successfully Updated")
        else:
            flash("Cannot be edited")
        return redirect(url_for("get_titles"))


@app.route("/delete_title/<title_id>")
def delete_title(title_id):
    # check if the user has logged in
    if not ('user' in session):
        return render_template("404.html")
    creator = mongo.db.titles.find_one(
        {"created_by": session["user"], "_id": title_id})
    admin = mongo.db.users.find_one({"username": "admin"})
    # ensures only the creator can delete the title
    if creator or admin:
        mongo.db.titles.delete_one({"_id": ObjectId(title_id)})
        flash("Title Successfully Deleted")
    else:
        flash("Unsuccessful Deletion")
    return redirect(url_for("get_titles"))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    # check if the user has logged in
    if not ('user' in session):
        return render_template("404.html")
    creator = mongo.db.reviews.find_one(
        {"created_by": session["user"], "_id": review_id})
    admin = mongo.db.users.find_one({"username": "admin"})
    # ensures only the creator can delete the review
    if creator or admin:
        mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
        flash("Review Successfully Deleted")
    else:
        flash("Unsuccessful Deletion")
    return redirect(url_for("get_titles"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)