
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, validators
from wtforms.validators import DataRequired, Email, EqualTo


class FormularioRegistro(FlaskForm):
    nome = StringField('nome', validators=[
                       DataRequired('Por favor, insira seu nome.')])
    email = StringField('email', validators=[DataRequired(
        'Por favor, insira seu email.'), Email()])
    endereco = StringField('endereco', validators=[
                           DataRequired('Por favor, insira seu endereço.')])
    # FALTA TELEFONE
    senha1 = PasswordField('senha', [validators.DataRequired(), validators.Length(
        min=7, max=20, message="Senha muito longa máx de 20 characteres")])
    senha2 = PasswordField('confirmar senha', [validators.DataRequired(), validators.Length(
        min=7, max=20, message="Senha muito longa máx de 20 characteres"), EqualTo('senha1')])
    submit = SubmitField('registrar')


class FormularioLogin(FlaskForm):
    email = StringField('email', validators=[DataRequired(
        'Por favor, insira seu email.'), Email()])
    senha = PasswordField('senha', validators=[DataRequired()])
    remember = BooleanField('Lembre-me', validators=[DataRequired()])
    submit = SubmitField('login')


class FormularioPet(FlaskForm):
    nomePet = StringField('nome',
                          [
                              validators.Regexp(
                                  '[a-zA-Z]+', message="Nome deve conter somente letras"),
                              validators.Length(
                                  min=2, max=25, message="Nome deve ter entre 5 e 25 characteres")
                          ])
    idade = StringField('idade',
                        [
                            validators.Regexp(
                                '^[0-9]*$', message="idade deve conter somente números"),
                            validators.Length(
                                min=1, max=3, message="idade deve ter no máximo 3 dígitos")
                        ])
    especie = StringField('especie',
                          [
                              validators.Regexp(
                                  '[a-zA-Z]+', message="Espécie deve conter somente letras")
                          ])
    observacoes = StringField('observacoes',
                              [
                                  validators.Regexp(
                                      '^[a-zA-Z0-9_.-]*$', message=""),
                                  validators.Length(
                                      min=0, max=500, message="As observações devem ter no máximo 500 palavras")
                              ])
    user_id = IntegerField()
    submit = SubmitField('cadastrar')
