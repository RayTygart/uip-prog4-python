from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    if request.method == 'POST':
        resultado = request.form["Monto"]
        resp = make_response(render_template("resultado.html", Monto=resultado))
        resp.set_cookie('Monto', resultado)
        return resp

@app.route('/leercookie', methods=['GET'])
def leercookie():
     if request.method == 'GET':
         if 'Monto' in request.cookies:
             return 'Encontrado' + resp
         else:
             return 'No hay cookies disponibles'



         # Monto = request.form['Monto']
         # respuesta = make_response(render_template('leercookie.html'))
         # respuesta.set_cookie('Monto', Monto)
         # return respuesta
         #return render_template('leercookie.html')
if __name__ == '__main__':
    app.run()