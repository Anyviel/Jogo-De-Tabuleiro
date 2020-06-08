#Jogo de Tabuleiro feito como Avaliação da cadeira de Estrutura de Dados;
#O Tabuleiro é composto por 17 casas (0 à 16), tendo inicio na casa 0;
#Em determinadas casas, há prendas ou bônus, que atrasam ou auxiliam o jogador;
#Vence aquele que chega primeiro na casa 16;

from random import randint

tabuleiro = [{ 'acao': 'SAFE' }]*17

# PRENDAS
tabuleiro[4] = { 'acao': 'VOLTAR_DUAS' }
tabuleiro[9] = { 'acao': 'ESCOLHER_AVANCAR' }
tabuleiro[15] = { 'acao': 'VOLTAR_INICIO' }
# BÔNUS
tabuleiro[6] = { 'acao': 'AVANCE_CASA_10' }
tabuleiro[11] = { 'acao': 'AVANCE_UMA' }
tabuleiro[13] = { 'acao': 'ESCOLHER_VOLTAR' }


numero_jogadores = 0

while (numero_jogadores < 2 or numero_jogadores > 4): # Input da Quantidade de Jogadores
  numero_jogadores = int(input("Informe o Número de Jogadores (2-4): "))

jogadores = [0]*numero_jogadores

# Define qual o jogador deve jogar
turno = 0

def finished(): #Verifica se há um Vencedor
  return not all(pontos < 16 for pontos in jogadores)

def get_winner(): #Pega o Vencedor da Partida
  vencedor = None

  for i in range(numero_jogadores):
    if (jogadores[i] >= 16):
      vencedor = jogadores[i]
  
  return vencedor

def reset_loosers(): #Retorna os Perdedores para a Posição 00
  for i in range(numero_jogadores):
    if (jogadores[i] < 16):
      jogadores[i] = 0
  

def roll(): #Joga o Dado.
  return randint(1,6)

# Escolhe um jogador diferente do jogador do turno para fazer uma ação
def choose(text):
  jogador = int(input(f'Escolha um jogador para {text}: '))

  jogador = jogador - 1

  while (jogador == turno or jogador < 0 or jogador > numero_jogadores):
    if (jogador == turno):
      print('Você não pode escolher a si mesmo!')
    else:
      print(f'Você deve escolher um jogador entre 1 e {numero_jogadores}')
    jogador = int(input(f'Escolha um jogador para {text}'))
    jogador = jogador - 1
  
  return jogador

def get_tabuleiro():
  tab = "|00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|\n"

  for i in range(numero_jogadores):
    tab = tab + "|"
    for j in range(17):
      if (jogadores[i] == j):
       tab = f'{tab}{(i+1):02}|'
      else:
        tab = f"{tab}  |"
    tab = f'{tab}\n'

  return tab

def print_tabuleiro(): # Imprime o tabuleiro com cada jogador em sua posição
  print(get_tabuleiro())

while(not finished()): # Enquanto NÃO houver um Vencedor o Jogo continua
  print_tabuleiro()

  if (jogadores[turno] >= 17):
    turno + 1
    if (turno >= numero_jogadores):
      turno = 0
    continue    
  
  print(f'\nVez do jogador: {turno + 1}')
  input('Aperte enter para jogar o dado: ')

  dado = roll()

  nova_casa = jogadores[turno] + dado
  jogadores[turno] = nova_casa

  print(f'Você tirou {dado} no dado e foi para a casa {nova_casa}!')

  
  if (nova_casa < 17): # Se o jogador ainda não ganhou, escolhe uma ação
    acao = tabuleiro[nova_casa]['acao']
    
    if (acao == 'SAFE'):
      pass
    elif (acao == 'VOLTAR_DUAS'):
      jogadores[turno] = nova_casa - 2
      print('PRENDA: Você voltou 2 casas')
    elif (acao == 'ESCOLHER_AVANCAR'):
      jogador = choose('avançar duas casas')
      jogadores[jogador] += 2
    elif (acao == 'VOLTAR_INICIO'):
      jogadores[turno] = 0
      print('PRENDA: Você voltou para o início')
    elif (acao == 'AVANCE_CASA_10'):
      jogadores[turno] = 10
      print('BONUS: Você avançou para a casa 10')
    elif (acao == 'AVANCE_UMA'):
      jogadores[turno] += 1
      print('BONUS: você avançou mais uma casa')
    elif (acao == 'ESCOLHER_VOLTAR'):
      jogador = choose('voltar duas casas')
      jogadores[jogador] = max(jogadores[jogador] - 2, 0)
  elif (nova_casa >= 16): # Se o jogador ganhou,  move pra ultima posição
    jogadores[turno] = 16

  vencedor = get_winner()
  
  if (vencedor is not None): # se houver um vencedor, todos os perdedores voltam pro inicio
    reset_loosers();
    print_tabuleiro();
    print(f" Parabéns! O Jogador {turno + 1} VENCEU!")
  else: # Se não houver vencedor, inicia um novo turno
    novo_turno = turno + 1

    if (novo_turno >= numero_jogadores):
      novo_turno = 0

    turno = novo_turno

f = open("resultado.txt", "w")
f.write(f"O Jogador {turno + 1} VENCEU! \n")
f.write(get_tabuleiro())
f.close()