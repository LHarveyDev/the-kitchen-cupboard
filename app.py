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


# Function runs when users navigate to Home using NavBar
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Function to allow users to search database using keyword
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    results = []
# If any results are found then return as a list
    if request.method == "POST" and query:
        results = list(mongo.db.recipes.find({"$text": {"$search": query}}))
# If no results are found display flash message and reload search page
    if not results and query:
        flash("No results found for '{}' Please try another search".format(
            query))

    return render_template("search.html", results=results, query=query)


# Function to allow new users to register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!")
    return render_template("register.html")


# Function to allow registered users to sign in
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


# Function displays the logged in users profile
@app.route("/profile")
def profile():
    # Check if the user is authenticated
    if 'user' not in session:
        return redirect(url_for("signin"))

    # Retrieve the user's information and recipes from the database
    username = session['user']
    user = mongo.db.users.find_one({"username": username})

    # Check if the user exists in the database
    if not user:
        flash("User not found")
        return redirect(url_for("signin"))

    # Retrieve recipes created by the user
    recipes = mongo.db.recipes.find({'created_by': username})

    return render_template(
        "profile.html", username=username, user=user, recipes=recipes)


# Function to allow logged in users to logout
@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))


# Function to allow registered users to add their own recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe_name = request.form.get("recipe_name")
        recipe_ingredients = request.form.get("recipe_ingredients")
        recipe_method = request.form.get("recipe_method")

        # Add semi-colon to the end of each line to ensure items
        # are displayed correctly on individual lines
        recipe_ingredients = ';'.join(recipe_ingredients.split('\n'))
        recipe_method = ';'.join(recipe_method.split('\n'))

        recipe = {
            "name": recipe_name,
            "ingredients": recipe_ingredients,
            "method": recipe_method,
            "created_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("add_recipe"))

    recipes = mongo.db.recipes.find().sort("name", 1)
    return render_template("add_recipe.html", recipes=recipes)


# Function to allow registered users to edit their own recipes
@app.route("/edit_recipe/<recipe_id>)", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if not recipe:
        flash("Recipe not found")
        return redirect(url_for("profile"))

    if request.method == "POST":
        # Update the recipe details in the database
        updated_recipe = {
            "name": request.form.get("recipe_name"),
            "ingredients": request.form.get("recipe_ingredients"),
            "method": request.form.get("recipe_method"),
            "created_by": session["user"]
        }

        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": updated_recipe})
        flash("Recipe Successfully Updated")
        return redirect(url_for("profile"))

    return render_template("edit_recipe.html", recipe=recipe)


# Function to allow registered users to delete their own recipes
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
