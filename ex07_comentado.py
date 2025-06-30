import tkinter as tk  # O velho e bom Tkinter, nosso construtor de janelas.
import pygame  # Chamando o pygame de novo, DJ oficial do projeto.

# Agora sim! Olha só, uma LISTA com dicionários organizados! Alguém assistiu aula de Python.
info_teclas_brancas = [
    {'tecla': ['Dó'], 'som': 'notas_simplificadas/do.wav'},
    {'tecla': ['Ré'], 'som': 'notas_simplificadas/re.wav'},
    {'tecla': ['Mi'], 'som': 'notas_simplificadas/mi.wav'},
    {'tecla': ['Fá'], 'som': 'notas_simplificadas/fa.wav'},
    {'tecla': ['Sol'], 'som': 'notas_simplificadas/sol.wav'},
    {'tecla': ['Lá'], 'som': 'notas_simplificadas/la.wav'},
    {'tecla': ['Si'], 'som': 'notas_simplificadas/si.wav'}
]
# 👆 A pessoa agora entendeu que repetição é feio, e que listas são melhores que lágrimas.

# Uma função que TAMBÉM amadureceu, mas ainda carrega o som toda vez...
def tocar_som(endereco):
    nota = pygame.mixer.Sound(endereco)  # Ainda carregando o som no clique, mas tudo bem, estamos progredindo.
    nota.play()

# Inicializando o pygame e seu sistema de som, como gente grande.
pygame.init()
pygame.mixer.init()

# Criação da nossa famosa janela "Piano Simples"
janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')  # Continua minúscula, mas ok.

# O forzinho maroto que cria os botões dinamicamente.
for posicao, item in enumerate(info_teclas_brancas):
    # ATENÇÃO: a parte com lambda pode parecer mágia antiga pra iniciantes
    # O lambda aqui captura o som correto... desde que você use o truque do `n=str(item['som'])`
    botao = tk.Button(janela, text=item['tecla'], command=lambda n=str(item['som']): tocar_som(n))
    botao.pack()

# E que comece o show!
janela.mainloop()
