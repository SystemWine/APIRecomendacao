from api.data.db_setup import db
from api.models import model_usuario

class UsuarioNotaVinhoModel(db.Model):
    __tablename__ = 'usuarionotavinhos'

    Id = db.Column(db.String, primary_key = True)
    IdUsuario = db.Column(db.String, nullable = False)
    IdVinho = db.Column(db.Integer, nullable = False)
    Nota = db.Column(db.Integer, nullable = False)    

    @classmethod
    def notas_por_usuario(cls, id_usuario):
        return cls.query.filter(UsuarioNotaVinhoModel.IdUsuario == id_usuario)

    @classmethod
    def avaliacoes(cls):
        notas = {}
        usuarios = model_usuario.Usuario.query.all()
        for user in usuarios:
            notas_user = {}

            for nota_vinho in cls.notas_por_usuario(user.Id):
                notas_user[nota_vinho.IdVinho] = nota_vinho.Nota

            notas[user.UserName] = notas_user
            
        return notas



# https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html        