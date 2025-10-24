from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def promedio():
    if request.method == 'POST':
        try:
            n1 = float(request.form['n1'])
            n2 = float(request.form['n2'])
            n3 = float(request.form['n3'])
            prom = (n1 + n2 + n3) / 3
            return f"El promedio de los números ingresados es {prom}"
        except ValueError:
            return "Por favor ingresa números válidos."
    return '''
        <form method="POST">
            Número 1: <input type="text" name="n1"><br>
            Número 2: <input type="text" name="n2"><br>
            Número 3: <input type="text" name="n3"><br>
            <input type="submit" value="Calcular promedio">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
