'''Programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
depois vai ler a quantidade de gols feito em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
from time import sleep
dic = dict()
lista = list()
dic['nome'] = str(input('Nome: ')).strip().capitalize()
quant = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for c in range(0, quant):
    lista.append(int(input(f'Quantos gols na partida {c + 1}? ')))
dic['gols'] = lista[:]
dic['total'] = sum(lista) # somando os elementos da lista
sleep(1)
print('-='*20)
print(dic)
print('-='*20)
for k, v in dic.items():
    sleep(1)
    print(f'O campo {k} tem o valor {v}.')
sleep(1)
print(f'O {dic["nome"]} jogou {quant} partida(s).')
for c in range(0, quant):
    sleep(1)
    print(f'  => Na partida {c+1}, fez {lista[c]} gol(s).')
print(f'Foi um total de {dic["total"]} gol(s).')
print('-='*20)
print('<<< ENCERROU >>>')
