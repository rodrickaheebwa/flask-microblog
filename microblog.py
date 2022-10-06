from app import app, db

from app.models import User, Post

# setting shell context to add our database instance for testing purposes as we build our app
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}