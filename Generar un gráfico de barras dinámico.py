# Importamos Flask, request y send_file
# Flask: para crear la aplicación web
# request: para acceder a los datos enviados desde el formulario
# send_file: para enviar archivos (en este caso la imagen del gráfico) al navegador
from flask import Flask, request, send_file

# Importamos matplotlib para generar gráficos
import matplotlib.pyplot as plt

# io nos permite trabajar con archivos en memoria (BytesIO) sin guardarlos en disco
import io

# Creamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal '/' que acepta métodos GET y POST
@app.route('/', methods=['GET', 'POST'])
def grafico():
    # Si se envía el formulario (POST)
    if request.method == 'POST':
        try:
            # Obtenemos los valores ingresados por el usuario y los convertimos a float
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
            tipo = request.form['tipo']  # Obtenemos el tipo de gráfico seleccionado
        except ValueError:
            # Si el usuario no ingresa números válidos
            return "Por favor ingresa números válidos."

        # Creamos una figura y un eje para dibujar el gráfico
        fig, ax = plt.subplots()

        # Dependiendo del tipo de gráfico seleccionado, dibujamos el gráfico correspondiente
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
            # Si el tipo de gráfico no es válido
            return "Tipo de gráfico no válido."

        # Guardamos el gráfico en un buffer en memoria en formato PNG
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)  # Movemos el puntero al inicio del buffer
        plt.close()  # Cerramos la figura para liberar memoria

        # Enviamos la imagen generada al navegador
        return send_file(buf, mimetype='image/png')

    # Si se accede por GET, mostramos el formulario HTML para que el usuario ingrese los datos
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

# Si ejecutamos este archivo directamente, iniciamos el servidor Flask en modo debug
if __name__ == '__main__':
    app.run(debug=True)
