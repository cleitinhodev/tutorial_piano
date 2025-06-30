"""
Isso funciona mas está errado! Não é elegante!
"""

import tkinter as tk
import pygame


def tocar_do():
    nota = pygame.mixer.Sound('notas_simplificadas/do.wav')
    nota.play()


def tocar_re():
    nota = pygame.mixer.Sound('notas_simplificadas/re.wav')
    nota.play()


def tocar_mi():
    nota = pygame.mixer.Sound('notas_simplificadas/mi.wav')
    nota.play()


def tocar_fa():
    nota = pygame.mixer.Sound('notas_simplificadas/fa.wav')
    nota.play()


def tocar_sol():
    nota = pygame.mixer.Sound('notas_simplificadas/sol.wav')
    nota.play()


def tocar_la():
    nota = pygame.mixer.Sound('notas_simplificadas/la.wav')
    nota.play()


def tocar_si():
    nota = pygame.mixer.Sound('notas_simplificadas/si.wav')
    nota.play()


pygame.init()
pygame.mixer.init()

janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

nota_do = tk.Button(janela, text='Tocar Dó', command=tocar_do)
nota_do.pack()
nota_re = tk.Button(janela, text='Tocar Ré', command=tocar_re)
nota_re.pack()
nota_mi = tk.Button(janela, text='Tocar Mi', command=tocar_mi)
nota_mi.pack()
nota_fa = tk.Button(janela, text='Tocar Fá', command=tocar_fa)
nota_fa.pack()
nota_sol = tk.Button(janela, text='Tocar Sol', command=tocar_sol)
nota_sol.pack()
nota_la = tk.Button(janela, text='Tocar Lá', command=tocar_la)
nota_la.pack()
nota_si = tk.Button(janela, text='Tocar Si', command=tocar_si)
nota_si.pack()

janela.mainloop()
