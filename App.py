# Import the Flask class from the flask module
from flask import Flask

# Import the "views" blueprint from the views module
from views import views 

# Create a Flask application instance
app = Flask(__name__)

# Register the "views" blueprint with a URL prefix of "/views"
app.register_blueprint(views, url_prefix="/views")

# Run the Flask application if this script is the main entry point
if __name__ == '__main__':
    # Start the application in debug mode on port 7000
    app.run(debug=True, port=7000)
