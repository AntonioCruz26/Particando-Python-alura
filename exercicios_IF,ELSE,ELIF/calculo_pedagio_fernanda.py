distancia_percorrida = int(input("Digite a distancia a ser percorrida (Km): "))

if distancia_percorrida <= 100:
    print("Valor pedágio: R$ 10,00")
elif 100 < distancia_percorrida <= 200:
    print("Valor pedágio: R$ 20,00")
else:
    print("Valor pedágio: R$ 30,00")