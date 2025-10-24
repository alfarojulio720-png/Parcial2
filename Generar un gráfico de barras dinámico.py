from flask import Flask, request, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def grafico():
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
            tipo = request.form['tipo']
        except ValueError:
            return "Por favor ingresa números válidos."

        fig, ax = plt.subplots()

        if tipo == 'barras':
            ax.bar(['A', 'B', 'C'], [a, b, c])
            ax.set_title("Gráfico de barras")
        elif tipo == 'linea':
            ax.plot(['A', 'B', 'C'], [a, b, c], marker='o')
            ax.set_title("Gráfico de línea")
        elif tipo == 'pastel':
            ax.pie([a, b, c], labels=['A', 'B', 'C'], autopct='%1.1f%%')
            ax.set_title("Gráfico de pastel")
        else:
            return "Tipo de gráfico no válido."

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        return send_file(buf, mimetype='image/png')

    return '''
        <form method="POST">
            Valor A: <input type="text" name="a"><br>
            Valor B: <input type="text" name="b"><br>
            Valor C: <input type="text" name="c"><br>
            Tipo de gráfico:
            <select name="tipo">
                <option value="barras">Barras</option>
                <option value="linea">Línea</option>
                <option value="pastel">Pastel</option>
            </select><br>
            <input type="submit" value="Generar gráfico">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
