from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return f"Hola, {nombre}! Bienvenido al sistema."
    return '''
        <form method="POST">
            Escribe tu nombre: <input type="text" name="nombre">
            <input type="submit" value="Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
