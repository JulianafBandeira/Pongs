import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import LoginManager, login_manager, current_user, login_required, login_user, logout_user
from flask import Flask, render_template, flash, redirect, url_for, request
from forms.forms import FormularioRegistro, FormularioLogin, FormularioPet
from models.user import User
from models.pet import Pets
from helpers.database import migrate, db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/pet"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager(app)
login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)


@app.before_first_request
def create_database():
     db.create_all()


@login_manager.user_loader
def load_user(user_id):
     return User.query.get(user_id) 

@app.route('/home')
def home():
    return render_template('user.html')

@app.route('/register', methods = ['POST','GET'])
def register():
    form = FormularioRegistro()
    if form.validate_on_submit():
        user = User(nome=form.nome.data, email=form.email.data, endereco=form.endereco.data, senha_hash=form.senha1.data)
        user.set_senha(form.senha1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormularioLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_senha(form.senha.data):
            login_user(user)
            proximo = request.args.get("proximo")
            return redirect(proximo or url_for('home'))
        flash('Endereço de email e/ou senha inválidos.')    
    return render_template('login.html', form=form)


@app.route("/forbidden", methods=['GET', 'POST'])
@login_required
def protected():
    return redirect(url_for('forbidden.html'))

@app.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/cadastrarpet', methods=['GET', 'POST'])
def cadastroPet():
    form = FormularioPet()
    if form.validate_on_submit():
        user_id = current_user.id
        pet = Pets(nome=form.nomePet.data, idade=form.idade.data, especie=form.especie.data, observacoes=form.observacoes.data, user_id=user_id)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('cadastropet.html', form=form)

# def check_pet():
#     allpets = Pets.query.all()
#     lista_pets = []
#     if pets in allpets:
#         pet_info = {
#             'id': pets.id,
#             'nome': pets.nome,
#             'idade': pets.idade,
#             'especie': pets.especie,
#             'observacoes': pets.observacoes
#         }
#         lista_pets.append(pet_info)
        
#         flash('Pet já cadastrado.')
#         return redirect(url_for('cadastroPet'))


@app.route('/allpets/', methods=['GET', 'POST'])
@login_required
def getPet():
    #ID USER CAPTURADO
    if current_user.is_authenticated:
        user = User()
        user.current_user_id = current_user.id
        current_user_id = user.current_user_id
        #pegando ID via-current_id
        # user1 = User.query.get(current_user_id)

        # pet_test = Pets()
        # user = pet_test.user1
        # pet_user_id_ = Pets.query.get(user)

        pet = Pets()
        #LISTA DE PETS
        allpets = Pets.query.all()

        lista_pets = []
        for pet in allpets:

            pet_info = {
                'id': pet.id,
                'nome': pet.nome,
                'idade': pet.idade,
                'especie': pet.especie,
                'observacoes': pet.observacoes
            }
            lista_pets.append(pet_info)

            #return redirect(f'/allpets/{pet_user_id_}')
        return render_template('pet.html', allpets=lista_pets)


@app.route('/allpets/', methods=['POST'])
@login_required

def deletePet():
    if current_user.is_authenticated:

        pet = Pets.query.first()
        if pet:
            # db.session.delete(pet)
            # db.session.commit()
            # return redirect(url_for('home'))
            return pet.id
        else:
            return flash('Nao encontrado')
    else:
        return redirect(url_for('forbidden'))




if __name__ == "__main__":
    app.run(debug=True)