from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, validators
from wtforms.validators import DataRequired, Email, EqualTo


class FormularioRegistro(FlaskForm):
    nome = StringField('nome', validators =[DataRequired('Por favor, insira seu nome.')])
    email = StringField('email', validators=[DataRequired('Por favor, insira seu email.'), Email()])
    endereco = StringField('endereco', validators=[DataRequired('Por favor, insira seu endereço.')])
    #FALTA TELEFONE
    senha1 = PasswordField('senha', [validators.DataRequired(), validators.Length(min=7,max=20,message="Senha muito longa máx de 20 characteres")])
    senha2 = PasswordField('confirmar senha', [validators.DataRequired(), validators.Length(min=7,max=20,message="Senha muito longa máx de 20 characteres"), EqualTo('senha1')])
    submit = SubmitField('registrar')


class FormularioLogin(FlaskForm):
    email = StringField('email',validators=[DataRequired('Por favor, insira seu email.'), Email()])
    senha = PasswordField('senha', validators=[DataRequired()])
    remember = BooleanField('Lembre-me',validators= [DataRequired()])
    submit = SubmitField('login')
    

class FormularioPet(FlaskForm):
    nomePet = StringField('nome', validators =[DataRequired()])
    idade = StringField('idade', validators =[DataRequired()])
    especie = StringField('especie', validators =[DataRequired()])
    observacoes = StringField('observacoes', validators =[DataRequired()])
    user_id = IntegerField()
    submit = SubmitField('cadastrar')
