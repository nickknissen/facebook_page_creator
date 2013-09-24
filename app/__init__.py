from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# Create Flask application
app = Flask(__name__)


# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
	lambda filename: url_for('static', filename = filename)
)

app.config.from_object('config')
db = SQLAlchemy(app)



from app import views