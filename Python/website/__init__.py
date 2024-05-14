from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

from sqlalchemy import create_engine, MetaData


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
db = SQLAlchemy()


# engine = create_engine ("mysql+pymysql://peace:tiger@127.0.0.1/databases.db")

# db_uri = 'mysql+pymysql://root:root@db:3306/blogdatabase'

def create_app(): # This is going to create a flask application and return it
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db') ## Old Database
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@pba42blogdb.c6jtmnlypkzc.eu-west-1.rds.amazonaws.com:3306/blogdatabase' ## New Database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import User, Post
    

    with app.app_context():
        db.create_all()
        print("Created Database")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader # Sessions temporarily store data about the user's activity on a webpage. E.g, some websites open where you left off, stores info like your username and password so that you don't have to constantly log into your account every time. Sessions don't last for very long, maybe lasting about 30 days
    def load_user(id):
        return User.query.get(int(id)) # Allows me to access information about the user from my database by their id

    return app

    

# def create_database(app):
#     if not path.exists("website/" + DB_NAME):
#         db.create_all(app=app)
#         print("Created database!") <-- This code is outdated and does not work. Flask 3 no longer accepts an `app` agrument to methods like `create_all`. So  
