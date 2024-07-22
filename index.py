from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), unique=True, nullable=False)

class Plantilla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

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

@app.route('/Eliminatorias')
def Eliminatorias():
    return render_template('Eliminatorias.html')

@app.route('/court')
def Court():
    return render_template('Canchas.html')

@app.route('/canteen')
def Canteen():
    return render_template('Cantina.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos
    app.run(debug=True, host='127.0.0.2', port=3500)