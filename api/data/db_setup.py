from api import app
from flask_sqlalchemy import SQLAlchemy

...

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/devmedia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()