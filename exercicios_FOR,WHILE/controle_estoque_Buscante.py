"""
Você está desenvolvendo um sistema de controle de estoque para o Buscante. 
Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. 
Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível.
"""

quantidade = 9

for i in range(quantidade):
    quantidade -= 1
    if quantidade == 0:
        print("Estoque esgotado")
        break
    print("Venda Realizada !  Estoque: ", quantidade)
