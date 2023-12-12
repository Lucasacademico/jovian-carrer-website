# Importado a funcionalidade 'render_template' para conectar rota ao arquivo home.html da pasta template
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_jovian(): 
    # Saída da rota para o arquivo home.html usando o comando render_template
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)