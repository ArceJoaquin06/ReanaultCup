from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('Menu.html')

@app.route('/students')
def Students():
    return render_template('Alumnos.html')

@app.route('/Dt')
def Dt():
    return render_template('DT.html')

@app.route('/planner')
def Planner():
    return render_template('Planillero.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2', port=3500)