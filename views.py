# Import the Blueprint and render_template functions from the flask module
from flask import Blueprint, render_template

# Create a Blueprint named "views" with the current module's name
# The second argument "views" is the name of the blueprint package
views = Blueprint(__name__, "views")

# Define a route for the root URL ("/") using the "views" blueprint
# For example  "http://0.0.0.0:7000/views
@views.route("/")
def Home():
    # Render the "index.html" template and return the result
    return render_template("index.html")
