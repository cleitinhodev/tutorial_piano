import tkinter as tk
import pygame

# Lista contendo as informações das teclas brancas do piano
# Cada item é um dicionário com o nome da tecla e o caminho para o arquivo de som correspondente
info_teclas_brancas = [
    {'tecla': ['Dó'], 'som': 'notas_simplificadas/do.wav'},
    {'tecla': ['Ré'], 'som': 'notas_simplificadas/re.wav'},
    {'tecla': ['Mi'], 'som': 'notas_simplificadas/mi.wav'},
    {'tecla': ['Fá'], 'som': 'notas_simplificadas/fa.wav'},
    {'tecla': ['Sol'], 'som': 'notas_simplificadas/sol.wav'},
    {'tecla': ['Lá'], 'som': 'notas_simplificadas/la.wav'},
    {'tecla': ['Si'], 'som': 'notas_simplificadas/si.wav'}
]

# Função responsável por tocar o som correspondente ao endereço (arquivo) recebido como parâmetro
def tocar_som(endereco):
    nota = pygame.mixer.Sound(endereco)  # Carrega o arquivo de áudio
    nota.play()  # Executa a reprodução do som

# Inicialização dos módulos do pygame necessários para o funcionamento do mixer de áudio
pygame.init()
pygame.mixer.init()

# Criação da janela principal da interface
janela = tk.Tk()
janela.title('Piano Simples')  # Definição do título da janela

# Laço para criação dos botões correspondentes a cada tecla branca do piano
for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(
        janela,
        text=item['tecla'],           # Texto exibido no botão (nome da nota)
        font=('Arial', 12),           # Fonte e tamanho do texto
        width=5,                     # Largura do botão em caracteres
        height=9,                    # Altura do botão em linhas (proporcional)
        background='white',          # Cor de fundo branca para simular tecla de piano
        bd=4,                       # Largura da borda do botão
        relief='raised',             # Estilo da borda para efeito tridimensional
        anchor=tk.S,                 # Alinha o texto na parte inferior do botão
        command=lambda n=str(item['som']): tocar_som(n)  # Associa o clique à função que toca o som
    )
    # Posiciona o botão na janela usando grid, alinhando na mesma linha e diferentes colunas
    botao.grid(row=0, column=posicao)

# Inicia o loop principal da interface, mantendo a janela ativa e aguardando interações do usuário
janela.mainloop()
