from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">Página inicial</a>  |  <a href="/sobre"</a>  |  <a href="/contato">Contato</a> 
<br>
"""

@app.route("/")
def hello_world():
  return "Olá, mundo! Este é meu site. (Manoela Bonaldo)"

@app.route("/sobre")
def sobre():
  return "Aqui vai o conteúdo da página sobre"

@app.route("contato")
def contato():
  return "Aqui vai o conteúdo da página contato"
