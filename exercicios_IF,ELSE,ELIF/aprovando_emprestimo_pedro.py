renda_mensal = float(input("Digite a sua renda mensal (R$): "))
parcela_desejada = float(input("Digite o valor da parcela desejada (R$): "))

if renda_mensal <= 2000:
    print("Emprestimo Negado: renda abaixo de R$ 2000,00")
elif parcela_desejada >= 0.3 * renda_mensal:
    print("Emprestimo Negado: parcela acima de 30% da renda")
else: 
    print("Emprestimo Aprovado!")