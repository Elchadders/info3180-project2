from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:password@localhost/musketeers"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cdmzfoncmoxpkz:bf997798c28f70567096e0d8fadd7e2fb8e6a1e5bca651f15baacf6a3d69789a@ec2-54-225-118-55.compute-1.amazonaws.com:5432/d1h8sc4k9uc6ls"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['USER_UPLOAD_FOLDER'] = "./app/static/uploads/users/"

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

app.config.from_object(__name__)
from app import views
