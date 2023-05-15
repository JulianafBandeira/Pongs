from helpers.database import db
from flask_login import UserMixin


class Pet(UserMixin, db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    idade = db.Column(db.String(4))
    especie = db.Column(db.String())  # TODO: Criar a entidade Especie
    # TODO: transformar num relacionamento 1..n
    observacoes = db.Column(db.String(500))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship("User", uselist=False)

    def __init__(self, nome, idade, especie, observacoes, user):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.observacoes = observacoes
        self.user = user
