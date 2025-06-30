import tkinter as tk
import pygame
from tkinter import ttk

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


def carregar_sons(lista):
    # Retorna um dicionário com o caminho do som como chave e o objeto Sound como valor
    return {i['som']: pygame.mixer.Sound(i['som']) for i in lista}


def tocar_som(endereco):
    nota = sons_cache.get(endereco)   # armazena a nota com base no endereço (Aqui a nota ja é um objeto carregado)
    if nota:   # Se a nota de fato existe no sistema, então é tocada.
        nota.play()


def resetar_teclas():
    for tecla in list(teclas_ativas):
        if tecla in botoes_associados:
            btn = botoes_associados[tecla]
            btn.config(relief='raised')
            btn.config(bg='black' if btn['bg'] == '#8accfe' else 'white')
        teclas_ativas.discard(tecla)


def tecla_pressionada(event):
    tecla = event.keysym   # Traz a informação de qual botão foi pressionado
    if tecla in botoes_associados and tecla not in teclas_ativas:   # Se botão existe e não esta ativado
        teclas_ativas.add(tecla)   # Adiciona o botão na lista de ativos
        btn = botoes_associados[tecla]   # captura o botão e armazena nesta variável
        btn.config(relief='sunken')   # Muda a borda pressionado
        if btn['bg'] == 'black':
            btn.config(bg='#8accfe')  # Cor mais escura para tecla preta
        else:
            btn.config(bg='#deb1e9')  # Cor cinza para tecla branca
        for letra in todas_as_teclas:   # Busca a tecla na lista e aciona a função para tocá-la
            if tecla in letra['tecla']:
                tocar_som(letra['som'])   # letra['som'] é o endereço do arquivo 'notas/c.wav'
                return   # # evita tocar duas vezes caso haja repetição


def tecla_liberada(event):
    tecla = event.keysym   # Traz a informação de qual botão foi liberado

    # Se for a tecla morta, forçamos o reset de tudo
    if tecla == '´' or tecla == 'Multi_key':
        resetar_teclas()
        return

    if tecla in botoes_associados:
        teclas_ativas.discard(tecla)   # Remove o botão da lista de ativos
        btn = botoes_associados[tecla]  # captura o botão e armazena nesta variável
        btn.config(relief='raised')   # Volta a aparência do botão aos estágio inicial
        btn.config(bg='black' if btn['bg'] == '#8accfe' else 'white')


# Função para ajustar volume (0.0 a 1.0)
def ajustar_volume(valor):
    volume = float(valor) / 100
    for som in sons_cache.values():
        som.set_volume(volume)


pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(64)

sons_cache = {**carregar_sons(info_teclas_brancas), **carregar_sons(info_teclas_pretas)}   # Sons pré-carregados

janela = tk.Tk()
janela.title('Piano Simples')
janela.resizable(False, False)

teclas_ativas = set()   # Botões ativos no momento
botoes_associados = {}   # Botões criados e assicioados a teclas ex {'z': Botão 1, 'x': Botão 2...}
todas_as_teclas = info_teclas_pretas + info_teclas_brancas

teclado_completo = tk.Frame(janela)
teclado_completo.grid(row=0, column=0, padx=5, pady=5)

# Frame lateral direito
lado_direito = tk.Frame(janela)
lado_direito.grid(row=0, column=1, padx=5, pady=5)

# Rótulo de Volume
rotulo_volume = tk.Label(lado_direito, text="Volume", font=('Arial', 10))
rotulo_volume.pack()

# Barra de Volume com ttk
barra_volume = ttk.Scale(lado_direito,
                         from_=100,
                         to=0,
                         orient='vertical',
                         command=ajustar_volume)
barra_volume.set(100)  # Volume inicial
barra_volume.pack(pady=5)

for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(teclado_completo,
                      text=item['tecla'][0],
                      font=('Arial', 12),
                      width=5,
                      height=9,
                      background='white',
                      bd=4,
                      relief='raised',
                      anchor=tk.S,
                      command=lambda n=str(item['som']): tocar_som(n))
    botao.grid(row=0, column=posicao)
    for t in item['tecla']:   # A cada botão criado, armazena em um dicionário
        botoes_associados[t] = botao   # A chave é o própria string ex: 'z', 'x', e o item é o objeto inteiro


# Criação das teclas pretas, que são posicionadas sobre as brancas
for item in info_teclas_pretas:
    botao = tk.Button(teclado_completo,
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
    x = int(item['posicao'] * 60)  # Calcula a posição horizontal
    botao.place(x=x, y=0)  # Posiciona usando coordenadas absolutas
    for t in item['tecla']:
        botoes_associados[t] = botao  # Associa tecla ao botão


janela.bind_all('<KeyPress>', tecla_pressionada)   # Verifica a todo momento se uma tecla é pressionada
janela.bind_all('<KeyRelease>', tecla_liberada)    # Verifica a todo momento se uma tecla é solta

janela.mainloop()
