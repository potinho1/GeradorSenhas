import random

minu = "abcdefghijklmnopqrstuvwxyz"
maiu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
simbolos = "[]{}()*#$%;/_-"

qntd = int(input("Digite o tamanho da sua senha: "))
qntdInt = int(qntd)
length = qntdInt

all = minu + maiu + num + simbolos
passwordAll = "".join(random.sample(all, length))

print(passwordAll)
