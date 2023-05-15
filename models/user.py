from helpers.database import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(150), unique=True)
    endereco = db.Column(db.String())
    senha_hash = db.Column(db.String())
    entrada_em = db.Column(db.DateTime(), default=datetime.utcnow)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
