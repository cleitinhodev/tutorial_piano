import tkinter as tk
import pygame

info_teclas_brancas = [
    {'tecla': ['z'], 'som': 'notas/c1.wav'},
    {'tecla': ['x'], 'som': 'notas/d1.wav'},
    {'tecla': ['c'], 'som': 'notas/e1.wav'},
    {'tecla': ['v'], 'som': 'notas/f1.wav'},
    {'tecla': ['b'], 'som': 'notas/g1.wav'},
    {'tecla': ['n'], 'som': 'notas/a1.wav'},
    {'tecla': ['m'], 'som': 'notas/b1.wav'}
]


def tocar_som(endereco):
    nota = pygame.mixer.Sound(endereco)
    nota.play()


def tecla_pressionada(event):
    tecla = event.keysym   # Traz a informação de qual botão foi pressionado
    if tecla in botoes_associados and tecla not in teclas_ativas:   # Se botão existe e não esta ativado
        teclas_ativas.add(tecla)   # Adiciona o botão na lista de ativos
        btn = botoes_associados[tecla]   # captura o botão e armazena nesta variável
        btn.config(relief='sunken')   # Muda a borda pressionado
        btn.config(bg='#d8c2ff')   # Muda a cor para mais escura
        for letra in info_teclas_brancas:   # Busca a tecla na lista e aciona a função para tocá-la
            if tecla in letra['tecla']:
                tocar_som(letra['som'])   # letra['som'] é o endereço do arquivo 'notas/c.wav'


def tecla_liberada(event):
    tecla = event.keysym   # Traz a informação de qual botão foi liberado
    if tecla in botoes_associados:
        teclas_ativas.discard(tecla)   # Remove o botão da lista de ativos
        btn = botoes_associados[tecla]  # captura o botão e armazena nesta variável
        btn.config(relief='raised')   # Volta a aparência do botão aos estágio inicial
        btn.config(background='white')


pygame.init()
pygame.mixer.init()

janela = tk.Tk()
janela.title('Piano Simples')

teclas_ativas = set()   # Botões ativos no momento
botoes_associados = {}   # Botões criados e assicioados a teclas ex {'z': Botão 1, 'x': Botão 2...}

for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(janela,
                      text=item['tecla'],
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


janela.bind_all('<KeyPress>', tecla_pressionada)   # Verifica a todo momento se uma tecla é pressionada
janela.bind_all('<KeyRelease>', tecla_liberada)    # Verifica a todo momento se uma tecla é solta

janela.mainloop()
