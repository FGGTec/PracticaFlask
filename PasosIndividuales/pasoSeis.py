from flask import Flask
app = Flask(__name__)
@app.route('/wellcome/<name>/<int:ncontrol>')
def hello(name, ncontrol):
    return f'Bienvenido {name}, tu número es: {ncontrol}'