"""
João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.
"""


while True:
    nome = input("Digite o seu nome: ")
    senha = input("Digite a sua senha: ")
    if len(nome) < 5:
        print("Digite um nome com pelo menos 5 caracteres")
        continue
    elif len(senha) < 8:
        print("Digite uma senha com pelo menos 8 caaracteres")
        continue
    elif len(nome) >= 5 and len(senha) >= 8:
        break
print("Cadastro realizado com sucesso!!")
