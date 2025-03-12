nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

print("\n Média: ", media)
if media < 5:
    print("Aluno Reprovado")
elif 5 <= media < 7:
    print("Aluno em Recuperação")
else:
    print("Aluno Aprovado")