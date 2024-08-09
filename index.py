from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar flash messages

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('Conection Uri: mysql://u4drvttmsnz01lkc:fea4CHjF009G1cs0NAqi@bnaj0hkpwqpowwit5aew-mysql.services.clever-cloud.com:3306/bnaj0hkpwqpowwit5aew') or 'mysql://u4drvttmsnz01lkc:fea4CHjF009G1cs0NAqi@bnaj0hkpwqpowwit5aew-mysql.services.clever-cloud.com/bnaj0hkpwqpowwit5aew'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

class Equipos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deporte_equipo = db.Column(db.String(50), unique=True, nullable=False)
    puntos_equipo = db.Column(db.Integer, nullable=False)
    grupo_equipo = db.Column(db.String(5), nullable=False)
    partidos_empatados = db.Column(db.Integer, nullable=False)
    partidos_ganados = db.Column(db.Integer, nullable=False)
    partidos_perdidos = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def principal():
    return render_template('Menu.html')

@app.route('/sports')
def Sports():
    return render_template('Deportes.html')

@app.route('/basket')
def Basket():
    return render_template('Basquet.html')

@app.route('/volley')
def Volley():
    return render_template('Voley.html')

@app.route('/football')
def Football():
    return render_template('Futbol.html')

@app.route('/register')
def Register():
    return render_template('Registro.html')

@app.route('/signIn')
def Signin():
    return render_template('IniciarSesion.html')

@app.route('/Eliminatorias')
def Eliminatorias():
    return render_template('Eliminatorias.html')

@app.route('/court')
def Court():
    return render_template('Canchas.html')

@app.route('/canteen')
def Canteen():
    return render_template('Cantina.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        flash('Login successful!', 'success')
        return redirect(url_for('principal'))
    else:
        flash('Invalid username or password', 'danger')
        return redirect(url_for('Register'))

if __name__ == '__main__':
    app.run(debug=True, port=3500)
