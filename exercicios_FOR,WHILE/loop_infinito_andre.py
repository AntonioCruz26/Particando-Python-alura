"""
André está testando um novo recurso no backend do Buscante que processa dados em um loop. 
Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

----Código do André----
contador = 0

while contador < 10:
    print("Processando dados...")

"""

#Código correto

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1