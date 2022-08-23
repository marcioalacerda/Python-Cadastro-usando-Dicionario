'''Aprimorando o programa para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador'''
from time import sleep
dic = dict()
lista = list()
campeonato = list()
while True:
    print('-'*40)
    dic['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    quant = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    for c in range(0, quant):
        lista.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    dic['gols'] = lista[:]
    dic['total'] = sum(lista)
    lista.clear()
    campeonato.append(dic.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
sleep(1)
print('-='*20)
#pode ser feito desta maneira também
#print(f'{"Cod":<4}{"Nome":<10}{"Gols":<20}{"Total":>6}')
print('Cod ', end='')
for i in dic.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for i, v in enumerate(campeonato):
    sleep(1)
    # pode ser feito desta maneira também
    #print(f'{i:<4}{campeonato[i]["nome"]:<10}{campeonato[i]["gols"]}{campeonato[i]["total"]:>19}')
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    pesquisa = int(input('Mostrar dados de qual jogador? (Digite o Cod.)(para sair 999) '))
    while pesquisa > len(campeonato)-1 and pesquisa != 999:
        print(f'ERRO! Não existe jogador com o codigo {pesquisa}! Tente novamente.')
        print('-' * 40)
        pesquisa = int(input('Mostrar dados de qual jogador? (Digite o Cod.)(para sair 999) '))
    if pesquisa == 999:
        break
    print(f'-LEVANTAMENTO DO JOGADOR {campeonato[pesquisa]["nome"]}-')
    print(f'O {campeonato[pesquisa]["nome"]} jogou {len(campeonato[pesquisa]["gols"])} partida(s).')
    for i, g in enumerate(campeonato[pesquisa]['gols']):
        sleep(1)
        print(f'  => Na partida {i+1}, fez {g} gol(s).')
    print(f'Foi um total de {campeonato[pesquisa]["total"]} gol(s).')
    print('-='*20)
print('<<< VOLTE SEMPRE >>>')
