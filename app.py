# Importado biblioteca jsonify que converte objetos Python em formato JSON
from flask import Flask, render_template, jsonify

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
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


# Rota que possibilita verificarmos os dados do DB do site em JSON
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
