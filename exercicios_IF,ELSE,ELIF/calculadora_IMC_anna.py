peso = int(input("digite o seu peso (KG): "))
altura = float(input("Digite a sua altura (M): "))
IMC = peso/(altura**2)

if IMC < 18.5:
    print("IMC: ", IMC, " // Situação: abaixo do peso")
elif 18.5 <= IMC < 25:
    print("IMC: ", IMC, " // Situação: peso normal")
else: 
    print("IMC: ", IMC, " // Situação: acima do peso")