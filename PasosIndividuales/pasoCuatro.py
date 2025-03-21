from flask import Flask
app = Flask(__name__)
@app.route('/wellcome/<int:ncontrol>')
def hello(ncontrol):
    return 'Bienvenido '+str(ncontrol)