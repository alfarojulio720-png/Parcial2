# Importamos Flask y request desde el paquete flask
# Flask nos permite crear aplicaciones web y request nos permite acceder a los datos enviados desde el cliente (por ejemplo, desde un formulario)
from flask import Flask, request

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos una ruta '/' que acepta métodos GET y POST
# GET: cuando alguien abre la página
# POST: cuando alguien envía datos a través del formulario
@app.route('/', methods=['GET', 'POST'])
def promedio():
    # Verificamos si el método usado para la petición es POST
    if request.method == 'POST':
        try:
            # Obtenemos los valores enviados en el formulario y los convertimos a float
            n1 = float(request.form['n1'])
            n2 = float(request.form['n2'])
            n3 = float(request.form['n3'])
            
            # Calculamos el promedio de los tres números
            prom = (n1 + n2 + n3) / 3
            
            # Retornamos el resultado como texto
            return f"El promedio de los números ingresados es {prom}"
        
        # En caso de que el usuario no ingrese un número válido
        except ValueError:
            return "Por favor ingresa números válidos."
    
    # Si el método es GET, mostramos el formulario HTML para ingresar los números
    return '''
        <form method="POST">
            Número 1: <input type="text" name="n1"><br>
            Número 2: <input type="text" name="n2"><br>
            Número 3: <input type="text" name="n3"><br>
            <input type="submit" value="Calcular promedio">
        </form>
    '''

# Si ejecutamos este archivo directamente, se inicia la aplicación en modo debug
# debug=True permite ver errores detallados y reinicia el servidor automáticamente al hacer cambios
if __name__ == '__main__':
    app.run(debug=True)
