# Enccontre todos os números primos possíveis partindo de 2 até a entrada colocada pelo criador do problema (11, no caso). Achei por bem colocar todos os números numa lista.

# 1 - COMO SABER SE UM NÚMERO É PRIMO OU NÃO EM CÓDIGO
# 2 - COLOCAR OS NÚMEROS PRIMOS NUMA LISTA DENTRO DE UMA FUNÇÃO CHAMADA PRIME_FINDER
# 3 - EXIBIR ESSA LISTA

lista = list() #lista dos números primos de 1 até 11
total = 0 #quantidade de vezes que um número é divisível
numero = 2
quantidade = 1

def prime_finder(n):
    lista = list()
    numero = 2
    total = 1
    contador = 0
    while contador < n:
        if numero % 2 == 0:
            total += 1
            numero += 1
            lista.append(numero)
        contador += 1
    return lista
print(prime_finder(11)) # Você ativa a função, pelo menos nesse caso, pelo parâmetro (n).