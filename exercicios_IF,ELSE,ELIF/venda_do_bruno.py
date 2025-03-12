macas = int(input("Digite o numero de vendas das maças: "))
bananas = int(input("Digite o numero de vendas das bananas: "))

if macas > bananas:
    print("As maças vendaram mais")
elif bananas > macas:
    print("As bananas venderam mais")
else:
    print("Ambas venderam a mesma quantidade")