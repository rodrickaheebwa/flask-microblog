The microblog.py imports and runs the app(flask instance in __init__.py) from app folder(which is now a package since it contains an __init__.py file)

The app folder/package is our main point of emphasis.

__init__.py imports our routes.py where all our routes and the corresponding view functions are defined.
These can esentially be one file.

forms.py defines a flask form that we'll use on our webpage.

config.py
    Configuration is normally set from environment variables. If the environment variable is not found, we give a fallback value.
    The Flask-SQLAlchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI configuration variable.