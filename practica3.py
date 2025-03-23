from flask import Flask, json
app = Flask(__name__)
@app.route("/dict/<path:diccio>")
def show_d(diccio):
    diccionario = json.loads(diccio)
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario
@app.route("/tup/<path:tupl>")
@app.route("/tup/<path:tupl>")
def show_t(tupl):
    try:
        # Reemplazar paréntesis por corchetes para procesar como lista
        tupla_str = tupl.replace("(", "[").replace(")", "]")
        # Convertir a tupla
        tupla = tuple(eval(tupla_str))
        # Imprimir cada elemento de la tupla
        for tupV in tupla:
            print(f"{tupV}")
        # Devolver la tupla en formato de cadena con paréntesis
        return f'({", ".join(map(str, tupla))})', 200, {"Content-Type": "text/plain"}
    except SyntaxError:
        return "Formato de tupla inválido, use algo como (val1,val2)", 400, {"Content-Type": "text/plain"}
    except Exception as e:
        return f"Ocurrió un error: {str(e)}", 500, {"Content-Type": "text/plain"}
@app.route("/conj/<path:conjun>")
def show_c(conjun):
    try:
        # Reemplazar llaves {} por corchetes [] para procesar como una lista
        conjunto_str = conjun.replace("{", "[").replace("}", "]")
        # Convertir la lista en un conjunto
        conjunto = set(eval(conjunto_str))  # Convertir texto en un conjunto
        # Imprimir cada elemento del conjunto
        for elem in conjunto:
            print(f"{elem}")
        # Devolver el conjunto como una cadena representada con llaves {}
        return f'{{{", ".join(map(str, conjunto))}}}', 200, {"Content-Type": "text/plain"}
    except SyntaxError:
        return "Formato de conjunto inválido, use algo como {val1,val2}", 400, {"Content-Type": "text/plain"}
    except Exception as e:
        return f"Ocurrió un error: {str(e)}", 500, {"Content-Type": "text/plain"}
    

