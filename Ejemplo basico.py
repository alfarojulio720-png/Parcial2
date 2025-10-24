# Importamos Flask desde el paquete flask
from flask import Flask

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal '/' de la aplicación
# Esta función se ejecuta cuando alguien visita la URL principal
@app.route('/')
def home():
    # Retornamos un mensaje HTML simple que se mostrará en el navegador
    return '<h1>Hola, mundo desde Flask!</h1>'

# Si ejecutamos este archivo directamente, iniciamos el servidor Flask
if __name__ == '__main__':
    # debug=True permite ver errores detallados y reinicia el servidor automáticamente al hacer cambios
    app.run(debug=True)
