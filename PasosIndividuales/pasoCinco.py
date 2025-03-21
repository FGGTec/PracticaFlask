from flask import Flask
app = Flask(__name__)
@app.route('/wellcome/<int:ncontrol>')
def hello(ncontrol):
    return f'El número recibido es: {ncontrol}'