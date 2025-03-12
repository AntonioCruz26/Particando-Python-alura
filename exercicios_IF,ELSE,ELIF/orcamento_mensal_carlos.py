limite = 3000
despesas_mensal = float(input("Digite o valor da despesa desse mês (R$): "))

print("Despesa Mensal: ", despesas_mensal)
if despesas_mensal > limite:
    print("Atenção ! : Você ultrapassou o limite de despesas mensal")
elif despesas_mensal < limite:
    print("Você ainda está dentro do orçamento")
else: 
    print("orçamento exatamente no limite")