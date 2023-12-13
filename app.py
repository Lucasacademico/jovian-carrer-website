from flask import Flask, render_template

app = Flask(__name__)

# Estrutura de Banco de dados de empresas 
JOBS = [
    {
        'id': 1,
        'title': 'Data Analist',
        'location': 'Bengaluru, India',
        'salary': 'R$ 10000'
    },
    {
        'id': 2,
        'title': 'Front-End Engineer',
        'location': 'Delhi, India',
        'salary': 'R$ 15000'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Remote',
        'salary': 'R$ 12000'
    },
    {
        'id': 4,
        'title': 'Back-End Engineer',
        'location': 'San Francisco, USA',
        'salary': '$ 12000'
    }

]

@app.route("/")
def hello_jovian(): 
    # Passando a var do DB no retorno da rota
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)