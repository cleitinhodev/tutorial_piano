# Importa o módulo tkinter, usado para criar interfaces gráficas
import tkinter as tk

# Importa o módulo pygame, usado aqui para tocar os arquivos de som
import pygame

# Lista de teclas brancas do piano, com a tecla correspondente do teclado e o caminho do som
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

# Lista de teclas pretas, com teclas do teclado, som correspondente e posição em relação às brancas
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

# Função que carrega todos os arquivos de som de uma lista e retorna um dicionário
def carregar_sons(lista):
    return {i['som']: pygame.mixer.Sound(i['som']) for i in lista}

# Função que toca uma nota de acordo com o caminho passado
def tocar_som(endereco):
    nota = sons_cache.get(endereco)  # Recupera o objeto de som já carregado
    if nota:  # Se a nota existir
        nota.play()  # Toca o som

# Função chamada quando uma tecla do teclado é pressionada
def tecla_pressionada(event):
    tecla = event.keysym  # Obtém o nome da tecla pressionada
    if tecla in botoes_associados and tecla not in teclas_ativas:
        teclas_ativas.add(tecla)  # Marca como ativa
        btn = botoes_associados[tecla]  # Obtém o botão correspondente
        btn.config(relief='sunken')  # Muda a aparência como pressionado

        # Muda a cor do botão dependendo do tipo
        if btn['bg'] == 'black':
            btn.config(bg='#8accfe')  # Cor clara para tecla preta
        else:
            btn.config(bg='#deb1e9')  # Cor clara para tecla branca

        # Procura o som correspondente à tecla pressionada
        for letra in todas_as_teclas:
            if tecla in letra['tecla']:
                tocar_som(letra['som'])  # Toca a nota
                return  # Para a busca após tocar a nota

# Função chamada quando uma tecla é solta
def tecla_liberada(event):
    tecla = event.keysym
    if tecla in botoes_associados:
        teclas_ativas.discard(tecla)  # Remove da lista de teclas ativas
        btn = botoes_associados[tecla]  # Obtém o botão associado
        btn.config(relief='raised')  # Restaura aparência original
        # Retorna a cor original
        btn.config(bg='black' if btn['bg'] == '#8accfe' else 'white')

# Inicialização dos módulos do pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(64)  # Define 64 canais de áudio simultâneos

# Junta os sons das teclas brancas e pretas em um único dicionário (cache)
sons_cache = {**carregar_sons(info_teclas_brancas), **carregar_sons(info_teclas_pretas)}

# Cria a janela principal com Tkinter
janela = tk.Tk()
janela.title('Piano Simples')

teclas_ativas = set()  # Armazena as teclas ativas no momento
botoes_associados = {}  # Dicionário que associa teclas do teclado aos botões
todas_as_teclas = info_teclas_pretas + info_teclas_brancas  # Lista com todas as teclas

# Criação dos botões das teclas brancas
for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(
        janela,
        text=item['tecla'][0],  # Mostra a letra principal no botão
        font=('Arial', 12),
        width=5,
        height=9,
        background='white',
        bd=4,
        relief='raised',
        anchor=tk.S,
        command=lambda n=str(item['som']): tocar_som(n)  # Função chamada ao clicar
    )
    botao.grid(row=0, column=posicao)  # Posiciona no grid
    for t in item['tecla']:  # Associa cada tecla ao botão
        botoes_associados[t] = botao

# Atualiza o layout para garantir que os widgets tenham tamanho definido
janela.update_idletasks()

# Criação das teclas pretas, que são posicionadas com coordenadas exatas sobre as brancas
for item in info_teclas_pretas:
    botao = tk.Button(
        janela,
        text=item['tecla'][0],
        font=('Arial', 12),
        width=3,
        height=7,
        bg='black',
        fg='white',
        bd=2,
        anchor=tk.S,
        relief='raised',
        command=lambda n=str(item['som']): tocar_som(n)
    )
    x = int(item['posicao'] * 60)  # Calcula a posição horizontal baseada no índice
    botao.place(x=x, y=0)  # Posiciona com coordenadas absolutas
    for t in item['tecla']:  # Associa teclas ao botão
        botoes_associados[t] = botao

# Associa os eventos de teclado às funções
janela.bind_all('<KeyPress>', tecla_pressionada)  # Tecla pressionada
janela.bind_all('<KeyRelease>', tecla_liberada)   # Tecla liberada

# Inicia o loop principal da interface (janela)
janela.mainloop()
