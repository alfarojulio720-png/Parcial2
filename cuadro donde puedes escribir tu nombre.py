# Importamos Flask y request desde el paquete flask
# Flask nos permite crear la aplicación web y request nos permite acceder a los datos enviados desde el formulario
from flask import Flask, request

# Creamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal '/' que acepta métodos GET y POST
@app.route('/', methods=['GET', 'POST'])
def home():
    # Si el método es POST (cuando el usuario envía el formulario)
    if request.method == 'POST':
        # Obtenemos el valor ingresado en el formulario con el nombre 'nombre'
        nombre = request.form['nombre']
        # Devolvemos un mensaje personalizado al usuario
        return f"Hola, {nombre}! Bienvenido al sistema."
    
    # Si el método es GET (cuando se carga la página por primera vez), mostramos un formulario HTML
    return '''
        <form method="POST">
            Escribe tu nombre: <input type="text" name="nombre">
            <input type="submit" value="Enviar">
        </form>
    '''

# Si ejecutamos este archivo directamente, iniciamos el servidor en modo debug
if __name__ == '__main__':
    app.run(debug=True)
