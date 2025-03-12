ativ_A = int(input("Digite quantos dias até concluir a atividade A: "))
ativ_B = int(input("Digite quantos dias até concluir a atividade B: "))
ativ_C = int(input("Digite quantos dias até concluir a atividade C: "))

if ativ_A < 0 or ativ_B < 0 or ativ_C <0 :
    print("Erro: os dias não podem ser negativos!!")
else: 
    print("Tempo total do projeto: ", ativ_A + ativ_B + ativ_C)