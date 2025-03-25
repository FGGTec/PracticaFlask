from flask import Flask, json
app = Flask(__name__)
@app.route("/dict/<path:diccio>")
def show_d(diccio):
    diccionario = json.loads(diccio)
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario
@app.route("/tup/<path:tupl>")
def show_t(tupl):
    try:
        tupla_str = tupl.replace("(", "[").replace(")", "]")
        tupla = tuple(eval(tupla_str))

        for tupV in tupla:
            print(f"{tupV}")

        return f'({", ".join(map(str, tupla))})', 200, {"Content-Type": "text/plain"}
    except SyntaxError:
        return "Formato de tupla inválido, use algo como (val1,val2)", 400, {"Content-Type": "text/plain"}
    except Exception as e:
        return f"Ocurrió un error: {str(e)}", 500, {"Content-Type": "text/plain"}
@app.route("/conj/<path:conjun>")
def show_c(conjun):
    try:
        conjunto_str = conjun.replace("{", "[").replace("}", "]")
        conjunto = set(eval(conjunto_str))

        for elem in conjunto:
            print(f"{elem}")

        return f'{{{", ".join(map(str, conjunto))}}}', 200, {"Content-Type": "text/plain"}
    except SyntaxError:
        return "Formato de conjunto inválido, use algo como {val1,val2}", 400, {"Content-Type": "text/plain"}
    except Exception as e:
        return f"Ocurrió un error: {str(e)}", 500, {"Content-Type": "text/plain"}