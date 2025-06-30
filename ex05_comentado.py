import tkinter as tk
import pygame  # Importa o pygame, que será usado para tocar sons


# Define a função que será chamada ao clicar no botão
def tocar_som():
    # Carrega o arquivo de áudio (nota DO) usando o mixer do pygame
    nota = pygame.mixer.Sound('notas_simplificadas/do.wav')

    # Reproduz o som carregado
    nota.play()


# Inicializa os módulos do pygame
pygame.init()  # Inicializa os recursos principais do pygame
pygame.mixer.init()  # Inicializa o sistema de som (mixer)

# Cria a janela principal
janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

# Cria um botão com o texto 'Tecla' que chama a função tocar_som quando clicado
botao_de_teste = tk.Button(janela, text='Tecla', command=tocar_som)
botao_de_teste.pack()  # Posiciona o botão na janela

# Inicia o loop principal da interface gráfica
janela.mainloop()
