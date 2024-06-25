from flask import Flask, render_template

app = Flask(__name__)

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
    app.run(debug=True, host='127.0.0.2', port=3500)