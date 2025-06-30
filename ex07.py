import tkinter as tk
import pygame

info_teclas_brancas = [
    {'tecla': ['Dó'], 'som': 'notas_simplificadas/do.wav'},
    {'tecla': ['Ré'], 'som': 'notas_simplificadas/re.wav'},
    {'tecla': ['Mi'], 'som': 'notas_simplificadas/mi.wav'},
    {'tecla': ['Fá'], 'som': 'notas_simplificadas/fa.wav'},
    {'tecla': ['Sol'], 'som': 'notas_simplificadas/sol.wav'},
    {'tecla': ['Lá'], 'som': 'notas_simplificadas/la.wav'},
    {'tecla': ['Si'], 'som': 'notas_simplificadas/si.wav'}
]


def tocar_som(endereco):
    nota = pygame.mixer.Sound(endereco)
    nota.play()


pygame.init()
pygame.mixer.init()

janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(janela, text=item['tecla'], command=lambda n=str(item['som']): tocar_som(n))
    botao.pack()

janela.mainloop()
