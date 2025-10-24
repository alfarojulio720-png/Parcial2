# Importamos las librerías necesarias
from flask import Flask, request, send_file  # Flask para la app web, request para leer datos del formulario, send_file para enviar archivos al cliente
from PIL import Image  # PIL (Pillow) para manipulación de imágenes
import io  # Para trabajar con archivos en memoria (BytesIO)

# Creamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal '/' que acepta métodos GET y POST
@app.route('/', methods=['GET', 'POST'])
def imagen_bn():
    # Si se envía el formulario (POST)
    if request.method == 'POST':
        url = request.form['url']  # Obtenemos la URL ingresada por el usuario
        
        try:
            # Descargamos la imagen desde la URL usando requests y la abrimos con PIL
            img = Image.open(io.BytesIO(requests.get(url).content))
            
            # Convertimos la imagen a blanco y negro
            img = img.convert("L")  
        except:
            # Si ocurre cualquier error (URL inválida, no es imagen, etc.)
            return "Error al cargar la imagen. Verifica la URL."

        # Creamos un buffer en memoria para guardar la imagen convertida
        buf = io.BytesIO()
        img.save(buf, format='PNG')  # Guardamos la imagen en formato PNG en el buffer
        buf.seek(0)  # Nos aseguramos de que el puntero del buffer esté al inicio

        # Enviamos la imagen convertida al navegador
        return send_file(buf, mimetype='image/png')

    # Si se accede a la página por GET, mostramos un formulario para ingresar la URL
    return '''
        <form method="POST">
            URL de la imagen: <input type="text" name="url"><br>
            <input type="submit" value="Convertir a blanco y negro">
        </form>
    '''

# Si ejecutamos este archivo directamente
if __name__ == '__main__':
    import requests  # Importamos requests aquí para poder descargar imágenes
    app.run(debug=True)  # Iniciamos el servidor en modo debug
