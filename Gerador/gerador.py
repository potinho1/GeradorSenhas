import json
import random



minu = "abcdefghijklmnopqrstuvwxyz"
maiu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
simbolos = "[]{}()*#$%;/_-"

pergunta = int(input("Quantas senhas deseja gerar? "))

for i in range(pergunta):

    Lugar_senha = input("Qual o lugar que você quer gerar a senha? ")

    qntd = int(input("Digite o tamanho da sua senha: "))
    qntdInt = int(qntd)
    length = qntdInt

    all = minu + maiu + num + simbolos
    passwordAll = "".join(random.sample(all, length))

    print(passwordAll)


with open('gerador.json', 'w') as json_file:
    json.dump(Lugar_senha, json_file) 
    json.dump(passwordAll, json_file)

