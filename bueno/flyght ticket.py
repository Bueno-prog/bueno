import math
import os
import random
from datetime import datetime
import requests

data=datetime.now()
data2 = data.strftime(" %d/%m/%Y e horario %H:%M")


capitais=["Brasilia","São Paulo","Rio de Janeiro","Rio branco","Porto Alegre","Florianópolis"]
precos=[1000.0, 850.0, 900.0,1150,1200,530]

print("\nSEJA BEM VINDO")
print("Aqui você irá escolher dentre as opções que vai ser mostrado abaixo, para a onde você vai querer viajar.")
print("Muito obrigado(a) pela preferencia")
print("E bom proveito de sua viagem")

print("\nescolha uma das capitais do Brasil para onde deseja viajar")
for i in range(6):
    print(f"{i+1}.{capitais[i]}-R${precos[i]}")

while True:
    escolha_capital=int(input("Digite o número correspondente à capital desejada (1 a 6): "))
    
    if 1<= escolha_capital <=6:
        break
    print("Escolha inválida. Por favor, insira um valor entre 1 e 6.")
os.system('cls')
valor_passagem = precos[escolha_capital-1]


while True:
    parcelas=int(input("Digite o número de parcelas desejado (1 a 12): "))

    if 1<= parcelas <= 12:
        break
    print("Número de parcelas inválido. Por favor, insira um valor entre 1 e 12.")
os.system('cls')
valorParcela = valor_passagem / parcelas


print("Compra confirmada!")
print("Sua passagem foi comprada com sucesso.")
print(f"Valor total: R${valor_passagem:.2f} ")
valor_passagem=math.sqrt(2)
print(f"Número de parcelas: {parcelas}")
print(f"Valor de cada parcela: R$ {valorParcela:.2f}")
valorParcela=math.sqrt(2)
print(f"data da compra: {data2}")
print(f"Destino: {capitais[escolha_capital-1]}")


def obter_localizacao():
    response = requests.get("https://ipinfo.io")
    data = response.json()
    return data

localizacao = obter_localizacao()
print("Localização atual:", localizacao["city"], localizacao["region"], localizacao["country"])