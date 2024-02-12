import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
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


# Function to allow users to search the database using a keyword
@app.route("/search", methods=["GET"])
def search():
    # Get the query parameter from the form
    query = request.args.get("query")

    # Initialize an empty list for results
    results = []

    # If a query is provided, perform the search
    if request.method == "GET" and query:
        # Store the query in the session
        session['last_query'] = query
        # Perform the search and get the results
        results = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    # If no results are found, display a flash message
    if not results and query:
        flash(
            "No results found for '{}' Please try another search".format(
                query))

    # Return the results and query to the template
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
        flash("Registration Successful!")

        # Redirect to the user's profile page
        return redirect(url_for("profile"))

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
                flash("Incorrect Password")
        else:
            # username doesn't exist
            flash("Not Yet Registered")

        return redirect(url_for("register"))

    return render_template("signin.html")


# Function to display the logged in users profile
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


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":

        # Split ingredients and method by lines
        ingredients = request.form.get("recipe_ingredients").splitlines()
        method = request.form.get("recipe_method").splitlines()

        recipe = {
            "image": request.form.get("recipe_image"),
            "name": request.form.get("recipe_name"),
            "difficulty": request.form.get("recipe_difficulty"),
            "ingredients": ingredients,
            "method": method,
            "created_by": session.get("user")
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile"))

    recipes = mongo.db.recipes.find().sort("name", 1)
    return render_template("add_recipe.html", recipes=recipes)


# Function to allow registered users to edit their own recipes
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if not recipe:
        flash("Recipe not found")
        return redirect(url_for("profile"))

    if recipe["created_by"] != session["user"]:
        flash("You are not allowed to edit this recipe")
        return redirect(url_for("profile"))

    if request.method == "POST":
        # Check if a new image URL is provided
        new_image = request.form.get("recipe_image")
        if not new_image:
            # If not, keep the original image from the database
            new_image = recipe["image"]
        # Update the recipe details in the database
        updated_recipe = {
            "image": new_image,
            "name": request.form.get("recipe_name"),
            "difficulty": request.form.get("recipe_difficulty"),
            "ingredients": request.form.get("recipe_ingredients").splitlines(),
            "method": request.form.get("recipe_method").splitlines(),
            "created_by": session["user"]
        }

        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": updated_recipe})
        flash("Recipe Successfully Updated")
        return redirect(url_for("profile"))

    # Displays ingredients and method on separate lines
    recipe["ingredients"] = "\n".join(recipe.get("ingredients", []))
    recipe["method"] = "\n".join(recipe.get("method", []))

    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Retrieve the recipe from the database
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Check if the recipe exists
    if recipe:
        # Check if the logged-in user matches the creator of the recipe
        if session.get('user') == recipe.get('created_by'):
            # Delete the recipe if the user is the creator
            mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
            flash("Recipe Successfully Deleted")
        else:
            # If the user is not the creator, display a flash message
            flash("You are not allowed to delete this recipe")
    else:
        # If the recipe doesn't exist, display a flash message
        flash("Recipe not found")

    # Redirect to the profile page regardless of the outcome
    return redirect(url_for("profile"))


# Function to allow logged in users to logout
@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
