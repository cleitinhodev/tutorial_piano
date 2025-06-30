# Piano Virtual em Python com Tkinter e Pygame
# Este script cria um piano simples com sons reais das notas musicais.
# As teclas do teclado do computador são associadas às teclas do piano.
# O projeto usa a biblioteca tkinter para interface gráfica e pygame para reprodução dos sons.

import tkinter as tk      # Tkinter para interface gráfica
import pygame             # Pygame para manipular áudio

# Lista com informações das teclas brancas do piano
# Cada dicionário contém a tecla do teclado associada e o caminho do som correspondente
info_teclas_brancas = [
    {'tecla': ['z'], 'som': 'notas/c1.wav'},
    {'tecla': ['x'], 'som': 'notas/d1.wav'},
    {'tecla': ['c'], 'som': 'notas/e1.wav'},
    {'tecla': ['v'], 'som': 'notas/f1.wav'},
    {'tecla': ['b'], 'som': 'notas/g1.wav'},
    {'tecla': ['n'], 'som': 'notas/a1.wav'},
    {'tecla': ['m'], 'som': 'notas/b1.wav'},
    {'tecla': ['q', 'comma'], 'som': 'notas/c2.wav'},
    {'tecla': ['w', 'period'], 'som': 'notas/d2.wav'},
    {'tecla': ['e', 'semicolon'], 'som': 'notas/e2.wav'},
    {'tecla': ['r'], 'som': 'notas/f2.wav'},
    {'tecla': ['t'], 'som': 'notas/g2.wav'},
    {'tecla': ['y'], 'som': 'notas/a2.wav'},
    {'tecla': ['u'], 'som': 'notas/b2.wav'},
    {'tecla': ['i'], 'som': 'notas/c3.wav'},
    {'tecla': ['o'], 'som': 'notas/d3.wav'},
    {'tecla': ['p'], 'som': 'notas/e3.wav'},
    {'tecla': ['´', 'Multi_key'], 'som': 'notas/f3.wav'},
    {'tecla': ['[', 'bracketleft'], 'som': 'notas/g3.wav'}
]

# Lista com informações das teclas pretas do piano
# Além da tecla e som, aqui temos também a 'posicao' relativa ao eixo x
info_teclas_pretas = [
    {'tecla': ['s'], 'som': 'notas/cd1.wav', 'posicao': 0.7},
    {'tecla': ['d'], 'som': 'notas/de1.wav', 'posicao': 1.7},
    {'tecla': ['g'], 'som': 'notas/fg1.wav', 'posicao': 3.6},
    {'tecla': ['h'], 'som': 'notas/ga1.wav', 'posicao': 4.6},
    {'tecla': ['j'], 'som': 'notas/ab1.wav', 'posicao': 5.6},
    {'tecla': ['2'], 'som': 'notas/cd2.wav', 'posicao': 7.5},
    {'tecla': ['3'], 'som': 'notas/de2.wav', 'posicao': 8.5},
    {'tecla': ['5'], 'som': 'notas/fg2.wav', 'posicao': 10.5},
    {'tecla': ['6'], 'som': 'notas/ga2.wav', 'posicao': 11.5},
    {'tecla': ['7'], 'som': 'notas/ab2.wav', 'posicao': 12.5},
    {'tecla': ['9'], 'som': 'notas/cd3.wav', 'posicao': 14.4},
    {'tecla': ['0'], 'som': 'notas/de3.wav', 'posicao': 15.4},
    {'tecla': ['=', 'equal'], 'som': 'notas/fg3.wav', 'posicao': 17.4}
]

# Função que carrega todos os sons da lista fornecida e retorna um dicionário com os sons prontos
def carregar_sons(lista):
    return {i['som']: pygame.mixer.Sound(i['som']) for i in lista}

# Função que toca uma nota musical a partir do cache de sons
def tocar_som(endereco):
    nota = sons_cache.get(endereco)
    if nota:
        nota.play()

# Função que reseta visualmente as teclas (usada quando tecla é liberada)
def resetar_teclas():
    for tecla in list(teclas_ativas):
        if tecla in botoes_associados:
            btn = botoes_associados[tecla]
            btn.config(relief='raised')
            btn.config(bg='black' if btn['bg'] == '#8accfe' else 'white')
        teclas_ativas.discard(tecla)

# Evento acionado ao pressionar uma tecla do teclado
def tecla_pressionada(event):
    tecla = event.keysym
    if tecla in botoes_associados and tecla not in teclas_ativas:
        teclas_ativas.add(tecla)
        btn = botoes_associados[tecla]
        btn.config(relief='sunken')
        if btn['bg'] == 'black':
            btn.config(bg='#8accfe')  # Azul para teclas pretas
        else:
            btn.config(bg='#deb1e9')  # Lilás para teclas brancas
        for letra in todas_as_teclas:
            if tecla in letra['tecla']:
                tocar_som(letra['som'])
                return  # Evita tocar mais de uma vez

# Evento acionado ao soltar uma tecla do teclado
def tecla_liberada(event):
    tecla = event.keysym
    if tecla == '´' or tecla == 'Multi_key':  # Teclas mortas no Linux
        resetar_teclas()
        return
    if tecla in botoes_associados:
        teclas_ativas.discard(tecla)
        btn = botoes_associados[tecla]
        btn.config(relief='raised')
        btn.config(bg='black' if btn['bg'] == '#8accfe' else 'white')

# Inicialização do pygame para trabalhar com som
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(64)  # Define número de canais de áudio simultâneos

# Pré-carrega todos os sons do piano em um cache
sons_cache = {**carregar_sons(info_teclas_brancas), **carregar_sons(info_teclas_pretas)}

# Criação da janela principal do Tkinter
janela = tk.Tk()
janela.title('Piano Simples')

# Estruturas auxiliares
teclas_ativas = set()           # Guarda quais teclas estão sendo pressionadas no momento
botoes_associados = {}          # Dicionário que associa teclas do teclado aos botões na tela
todas_as_teclas = info_teclas_pretas + info_teclas_brancas  # Lista completa para busca de sons

# Criação das teclas brancas
for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(janela,
                      text=item['tecla'][0],
                      font=('Arial', 12),
                      width=5,
                      height=9,
                      background='white',
                      bd=4,
                      relief='raised',
                      anchor=tk.S,
                      command=lambda n=str(item['som']): tocar_som(n))
    botao.grid(row=0, column=posicao)  # Usa grid para posicionar horizontalmente
    for t in item['tecla']:
        botoes_associados[t] = botao  # Associa todas as variações de tecla ao botão

# Criação das teclas pretas
for item in info_teclas_pretas:
    botao = tk.Button(janela,
                      text=item['tecla'][0],
                      font=('Arial', 12),
                      width=3,
                      height=7,
                      bg='black',
                      fg='white',
                      bd=2,
                      anchor=tk.S,
                      relief='raised',
                      command=lambda n=str(item['som']): tocar_som(n))
    x = int(item['posicao'] * 60)  # Calcula posição baseada na proporção
    botao.place(x=x, y=0)          # Usa coordenadas absolutas para sobrepor às teclas brancas
    for t in item['tecla']:
        botoes_associados[t] = botao  # Associa cada tecla de atalho ao botão

# Vincula os eventos de pressionar e soltar tecla do teclado à janela
janela.bind_all('<KeyPress>', tecla_pressionada)
janela.bind_all('<KeyRelease>', tecla_liberada)

# Inicia o loop principal da interface gráfica
janela.mainloop()
