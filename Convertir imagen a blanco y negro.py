from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def imagen_bn():
    if request.method == 'POST':
        url = request.form['url']
        try:
            img = Image.open(io.BytesIO(requests.get(url).content))
            img = img.convert("L")  # Blanco y negro
        except:
            return "Error al cargar la imagen. Verifica la URL."

        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        return send_file(buf, mimetype='image/png')

    return '''
        <form method="POST">
            URL de la imagen: <input type="text" name="url"><br>
            <input type="submit" value="Convertir a blanco y negro">
        </form>
    '''

if __name__ == '__main__':
    import requests
    app.run(debug=True)
