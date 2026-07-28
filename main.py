import requests
from flask import Flask, render_template,request

app = Flask(__name__)


def buscar_letras(banda, musica):
    url = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    resposta = requests.get(url)

    letra = resposta.json()["lyrics"]
    return letra





@app.route("/")
def home():
    
    letra = None
    nome_musica = request.args.get("Musica")
    nome_banda = request.args.get("Banda")

    

    if nome_musica and nome_banda:
        letra = buscar_letras(nome_banda, nome_musica)
        print(letra)
    else:
        print("letra não encontrada ):")

    return render_template("index.html", letra=letra)










if __name__ == "__main__":
    app.run(debug=True)