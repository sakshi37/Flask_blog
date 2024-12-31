import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_mail import Mail

# Initialize the app
app = Flask(__name__)

# Configure the app
app.config['SECRET_KEY'] = '32680ec3c6996aaf95df75b89c39c6a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


# Initialize the database
db = SQLAlchemy(app)
# Initialize hash Bcrypt
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME']= os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail =Mail(app)
app.app_context().push()


# Import routes at the end to avoid circular imports
from flask_blog import routes
