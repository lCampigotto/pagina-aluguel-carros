import csv   # já tinha feito esse sistema antes, só olhar no github --- link[https://github.com/lCampigotto/Codificador-de-Registro]


from flask import Flask
app = Flask(__name__)



def leitor_arquivo(caminho):
    with open(caminho) as dados:
        return list(csv.DictReader(dados))
        
def verificar_login(usuario, senha):
    for item in leitor_arquivo("dados.csv"):
        if usuario == item['usuario'] and senha == item['senha']:
            return True
    return False

def cadastrar_usuario(usuario, senha):
    with open("dados.csv", "a", newline='') as dados:
        writer = csv.writer(dados)
        writer.writerow([usuario, senha])

def codificar_usuario(usuario):
    resultado = ""
    for letra in usuario:
        if letra.isalpha():
            base = 97 if letra.islower() else 65
            letra_codificada = chr((ord(letra) - base + 10) % 26 + base)
            resultado += letra_codificada
        else:
            resultado += letra
    return resultado

def codificar_senha(senha):
    resultado = ""
    for numero in senha:
        if numero.isdigit():
            numero_codificado = str((int(numero) + 3) % 10)
            resultado += numero_codificado
        else:
            resultado += numero
    return resultado


@app.route('/')
def home():
    return 'Servidor funcionando!'
if __name__ == '__main__':
    app.run(debug=True)