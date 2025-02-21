from app import app, db
from app.models import Post, SetAnon, Set, User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': Post, 'SetAnon': SetAnon, 'User': User, 'Set': Set}
