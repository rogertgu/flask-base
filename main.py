import os

from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "mysecretkey"),
    # Otros ajustes de configuración si los necesitas
)

# rutas
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
