import os

import gspread
import requests
from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials
from tchan import ChannelScraper


TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]

with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key("1NuMnkxDYzf4CtKPzV1jbKDmwWbM5W7Bld3EqgM9IoHs")
sheet = planilha.worksheet("Página1")

app = Flask(__name__)


def ultimas_promocoes():
  scraper = ChannelScraper()
  contador = 0
  resultado = []
  for message in scraper.messages("promocoeseachadinhos"):
    contador += 1
    texto = message.text.strip().splitlines()[0]
    resultado.append(f"{message.created_at} {texto}")
    if contador == 10:
      return resultado
  
menu = """
<a href="/">Página inicial</a> | <a href="/arquivo_listasuja">Arquivo da Lista Suja</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return menu + "Olá, este é o site do robô do trabalho escravo."

@app.route("/sobre")
def sobre():
  return menu + "Aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
  return menu + "Aqui vai o conteúdo da página Contato"

@app.route("/arquivo-lista-suja")
def contato():
  return menu + "Aqui vai o conteúdo de arquivo da lista suja"


@app.route("/dedoduro")
def dedoduro():
  mensagem = {"chat_id": TELEGRAM_ADMIN_ID, "text": "Alguém acessou a página dedo duro!"}
  resposta = requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage", data=mensagem)
  return f"Mensagem enviada. Resposta ({resposta.status_code}): {resposta.text}"


@app.route("/dedoduro2")
def dedoduro2():
  sheet.append_row(["Manoela", "Bonaldo", "a partir do Flask"])
  return "Planilha escrita!"


@app.route("/telegram-bot", methods=["POST"])
def telegram_bot():
  update = request.json
    if message == "oi":
    texto_resposta = f"Olá. 🤖\n\nSou o robô do combate ao trabalho escravo.\n\nO que você deseja saber?\n\nDigite 1️⃣ para descobrir o número total de trabalhadores que constam na lista suja do trabalho escravo.\nDigite 2️⃣ para saber em quais atividades econômicas o trabalho análogo à escravidão é mais frequente.\nDigite 3️⃣ para descobrir qual foi o estado em que mais pessoas foram resgatadas.\nDigite 4️⃣ para denunciar casos de trabalho análogo à escravidão.\nDigite 5️⃣ para maiores informações sobre trabalho escravo e outras dúvidas. \n\n📊🔍Os dados analisados aqui são fornecidos pelo Ministério do Trabalho e Previdência do Brasil por meio do Cadastro de Empregadores que tenham submetido trabalhadores a condições análogas à de escravo (Lista Suja do Trabalho Escravo)."
  elif message == "1":
    texto_resposta = f"Infelizmente o trabalho análogo ao de escravo ainda é uma realidade no Brasil.\n\nNa lista suja mais atual, {int(Soma_Trabalhadores)} trabalhadores foram resgatados em condições análogas à escravidão."
  elif message == "2":
    texto_resposta = f"As atividades econômicas com maior frequência de trabalho escravo na lista suja mais atual são, respectivamente:\n\n{b['CNAE'].loc[0]}, \n{b['CNAE'].loc[1]}, \ne { b['CNAE'].loc[2]}."
  elif message == "3":
    texto_resposta = f"O estado com o maior número de trabalhadores em situação análoga a escravidão é {Trabalhadores_UF['UF'].loc[0]}, com um total de {int(Trabalhadores_UF['Trabalhadores envolvidos'].loc[0])} trabalhadores resgatados. \n\nEsse valor é referente à lista suja mais atual."
  elif message == "4":
    texto_resposta = f"O Ministério do Trabalho usa a plataforma IPÊ para coletar denúncias 🚨 de trabalho análogo à escravidão. O sigilo da denúncia é garantido e você pode realizá-la clicando no link a seguir. https://ipe.sit.trabalho.gov.br/#!/"
  elif message == "5":
    texto_resposta = f"A maioria dos trabalhadores que formam a mão de obra escrava é migrante, de baixa renda, oriunda de regiões marcadas pela fome e pobreza, onde há pouca oportunidade de sustento. \n\nLonge das estruturas de proteção social, eles são facilmente envolvidos por relações de trabalho violentas e têm sua força de trabalho extraída ao máximo. \n\nMuitos acabam sendo explorados e expostos a condições de trabalho degradantes, sem acesso à água potável, banheiro, comida de qualidade, sem um teto digno, vivendo sob ameaças e sem pagamento.\n\n⚖️ O Art. 149. do CP afirma ser crime reduzir alguém a condição análoga à de escravo quando há:  \n\n- Trabalho forçado; \n- Condições degradantes de trabalho; \n- Restrição de locomoção; \n- Servidão por dívida.  \n\nConsidera-se trabalho escravo quando alguma das situações é observada.\n\n📂 Para acessar a Lista Suja do Trabalho Escravo, acesse o link abaixo. www.gov.br/trabalho-e-previdencia/pt-br/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/combate-ao-trabalho-escravo-e-analogo-ao-de-escravo\n\n\n🤖 O robô do trabalho escravo foi desenvolvido por Manoela Bonaldo (📩 bonaldomanoela@gmail.com) para a disciplina de Algoritmos de Automação, dos professores Álvaro Justen e Guilherme Felitti, no Master em Jornalismo de Dados, Automação e Datastorytelling, no Insper.\n\n"

  else:
    texto_resposta = f"Olá. 🤖\n\nSou o robô do combate ao trabalho escravo.\n\nO que você deseja saber?\n\nDigite 1️⃣ para descobrir o número total de trabalhadores que constam na lista suja do trabalho escravo.\nDigite 2️⃣ para saber em quais atividades econômicas o trabalho análogo à escravidão é mais frequente.\nDigite 3️⃣ para descobrir qual foi o estado em que mais pessoas foram resgatadas.\nDigite 4️⃣ para denunciar casos de trabalho análogo à escravidão.\nDigite 5️⃣ para maiores informações sobre trabalho escravo e outras dúvidas. \n\n📊🔍Os dados analisados aqui são fornecidos pelo Ministério do Trabalho e Previdência do Brasil por meio do Cadastro de Empregadores que tenham submetido trabalhadores a condições análogas à de escravo (Lista Suja do Trabalho Escravo)."
  
  requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)
  return "ok"

