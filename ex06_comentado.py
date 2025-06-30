"""
Pedi pro ChatGPT comentar esse código, olha o resultado kkkkkkkkkkkkkk
"""

import tkinter as tk  # Chamamos o Tkinter para fazer a interface, coitado, mal sabe o que o espera
import pygame  # E o pygame pra tocar as notas, como um DJ de festa de aniversário.

# Agora começa o show do copia-e-cola! 🎹 Cada função toca uma notinha e carrega o arquivo do zero...

def tocar_do():
    nota = pygame.mixer.Sound('notas_simplificadas/do.wav')  # Sim, ele carrega o som TODA VEZ. Performance? Nunca nem vi.
    nota.play()  # E toca como se nada estivesse errado. Inocente.

def tocar_re():
    nota = pygame.mixer.Sound('notas_simplificadas/re.wav')  # "Mas professor, se funciona, por que está errado?"
    nota.play()  # Porque seu PC chora cada vez que repete isso.

def tocar_mi():
    nota = pygame.mixer.Sound('notas_simplificadas/mi.wav')  # Ctrl+C... Ctrl+V... Ctrl+C... Ctrl+V...
    nota.play()

def tocar_fa():
    nota = pygame.mixer.Sound('notas_simplificadas/fa.wav')  # Imagine carregar o mesmo som 300 vezes... parabéns.
    nota.play()

def tocar_sol():
    nota = pygame.mixer.Sound('notas_simplificadas/sol.wav')  # Chega um ponto que até o pygame pensa "sério isso?"
    nota.play()

def tocar_la():
    nota = pygame.mixer.Sound('notas_simplificadas/la.wav')  # Cada função é igualzinha, só muda a nota. Um crime contra a programação limpa.
    nota.play()

def tocar_si():
    nota = pygame.mixer.Sound('notas_simplificadas/si.wav')  # O Python já desistiu de te julgar.
    nota.play()

# Inicia o pygame e seu pobre mixer
pygame.init()
pygame.mixer.init()

# Cria a janela com o nome do piano que é simples demais até no código
janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')  # 300x200? Vai faltar espaço pra tanto botão, meu rei.

# Botões! Cada um com seu próprio clone de função, porque modularidade é só pra os fracos
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

# Loop final. Depois disso, o código está livre... até o próximo botão ser clicado.
janela.mainloop()
