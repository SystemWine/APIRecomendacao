from flask_restful import Resource, reqparse
from api.models.model_usuario_nota_vinho import UsuarioNotaVinhoModel
from api.libs.recomendacao import *

parser = reqparse.RequestParser()
parser.add_argument('id_usuario')
#https://flask-restful.readthedocs.io/en/latest/reqparse.html

class Teste(Resource):
    def get(self):
        data = parser.parse_args()
        id_usuario = data['id_usuario']
        return getRecomendacoesUsuario(id_usuario)

class ObterRecomendacoesUsuario(Resource):
    def get(self):
        data = parser.parse_args()
        id_usuario = data['id_usuario']
        print('****************************')
        print(data)
        print('****************************')

        return getRecomendacoesUsuario(id_usuario)