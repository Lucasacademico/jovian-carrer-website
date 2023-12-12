
# Biblioteca de importação Flask
from flask import Flask

# Aplicação simples do app flask
app = Flask(__name__)

# Rota simples flask com saída de dado "Hello, World"
@app.route("/")
def hello_world(): 
    return "<p>Hello, Oi!</p>"


# # Roda essa linha de código com python app.py 
# print(__name__)
# if __name__ == "__main__":
#     print("Estou dentro do if agora")
    
# Maneira de rodar a aplicação direto do arquivo com python app.py com debugger ativado
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)