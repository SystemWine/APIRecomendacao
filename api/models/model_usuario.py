from api.data.db_setup import db

class Usuario(db.Model):
    __tablename__ = 'aspnetusers'

    Id = db.Column(db.String, primary_key = True)
    UserName = db.Column(db.String, nullable = False)



# https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html        