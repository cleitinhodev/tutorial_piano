import tkinter as tk  # Biblioteca para criar interfaces gráficas
import pygame  # Biblioteca para manipulação de áudio

# Lista de dicionários que mapeia as teclas do teclado ('z', 'x', 'c'...)
# para os arquivos de áudio correspondentes às notas do piano
info_teclas_brancas = [
    {'tecla': ['z'], 'som': 'notas/c1.wav'},
    {'tecla': ['x'], 'som': 'notas/d1.wav'},
    {'tecla': ['c'], 'som': 'notas/e1.wav'},
    {'tecla': ['v'], 'som': 'notas/f1.wav'},
    {'tecla': ['b'], 'som': 'notas/g1.wav'},
    {'tecla': ['n'], 'som': 'notas/a1.wav'},
    {'tecla': ['m'], 'som': 'notas/b1.wav'}
]

# Função que carrega e toca o som a partir do caminho fornecido
def tocar_som(endereco):
    nota = pygame.mixer.Sound(endereco)  # Cria o objeto Sound para o arquivo indicado
    nota.play()  # Reproduz o som

# Função que é chamada sempre que uma tecla do teclado é pressionada
def tecla_pressionada(event):
    tecla = event.keysym  # Captura o nome da tecla pressionada (ex: 'z', 'x', etc)
    # Verifica se a tecla pressionada está entre os botões criados e se não está ativa (evita repetição)
    if tecla in botoes_associados and tecla not in teclas_ativas:
        teclas_ativas.add(tecla)  # Marca a tecla como ativa (pressionada)
        btn = botoes_associados[tecla]  # Recupera o botão associado a essa tecla
        btn.config(relief='sunken')  # Altera o estilo da borda para parecer pressionado
        btn.config(bg='#d8c2ff')  # Muda a cor do botão para indicar visualmente que está ativo
        # Busca na lista de teclas a que corresponde à tecla pressionada para tocar o som correto
        for letra in info_teclas_brancas:
            if tecla in letra['tecla']:
                tocar_som(letra['som'])  # Chama a função para reproduzir o som correspondente

# Inicialização dos módulos do pygame para áudio
pygame.init()
pygame.mixer.init()

janela = tk.Tk()  # Criação da janela principal da interface
janela.title('Piano Simples')  # Título da janela

teclas_ativas = set()  # Conjunto para controlar quais teclas estão ativas (pressionadas)
botoes_associados = {}  # Dicionário que associa cada tecla do teclado a seu botão gráfico correspondente

# Loop para criar os botões do piano e armazenar a associação tecla->botão
for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(
        janela,
        text=item['tecla'],         # Texto do botão (ex: 'z')
        font=('Arial', 12),         # Fonte do texto
        width=5,                   # Largura do botão
        height=9,                  # Altura do botão (para simular tecla de piano)
        background='white',         # Cor branca, simulando tecla branca
        bd=4,                      # Largura da borda
        relief='raised',            # Estilo da borda (levantada)
        anchor=tk.S,                # Texto ancorado na parte inferior do botão
        command=lambda n=str(item['som']): tocar_som(n)  # Ao clicar no botão, toca o som
    )
    botao.grid(row=0, column=posicao)  # Posiciona o botão na linha 0, coluna conforme posição
    for t in item['tecla']:  # Para cada tecla representada (normalmente uma só, como 'z')
        botoes_associados[t] = botao  # Armazena no dicionário para associar tecla física ao botão

# Configura a janela para verificar todas as teclas pressionadas no teclado físico
janela.bind_all('<KeyPress>', tecla_pressionada)

janela.mainloop()  # Inicia o loop principal do Tkinter para manter a janela ativa
