import os

from flask import Flask, flash, redirect, render_template, request

# Obtener el valor de cada variable de entorno
app_author = os.getenv("APP_AUTHOR", "Autor predeterminado")
app_name = os.getenv("APP_NAME", "Nombre de la aplicación predeterminado")

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "contraseñasuperfuerte"),
    # Otros ajustes de configuración si los necesitas
)

# rutas
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", app_author=app_author, app_name=app_name)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
