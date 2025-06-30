import tkinter as tk
import pygame


def tocar_som():
    nota = pygame.mixer.Sound('notas_simplificadas/do.wav')
    nota.play()


pygame.init()
pygame.mixer.init()

janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

botao_de_teste = tk.Button(janela, text='Tecla', command=tocar_som)
botao_de_teste.pack()

janela.mainloop()
