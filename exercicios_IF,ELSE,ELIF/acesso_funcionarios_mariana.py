horario_acesso = int(input("Digite o horario atual do acesso (formato 24H): "))

if 8 <= horario_acesso < 18:
    print("Acesso liberado!")
else: 
    print("Acesso negado!")