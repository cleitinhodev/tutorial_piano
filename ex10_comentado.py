import tkinter as tk  # Biblioteca para interface gráfica
import pygame  # Biblioteca para manipulação de áudio

# Mapeamento das teclas físicas do teclado para arquivos de som das notas do piano
info_teclas_brancas = [
    {'tecla': ['z'], 'som': 'notas/c1.wav'},
    {'tecla': ['x'], 'som': 'notas/d1.wav'},
    {'tecla': ['c'], 'som': 'notas/e1.wav'},
    {'tecla': ['v'], 'som': 'notas/f1.wav'},
    {'tecla': ['b'], 'som': 'notas/g1.wav'},
    {'tecla': ['n'], 'som': 'notas/a1.wav'},
    {'tecla': ['m'], 'som': 'notas/b1.wav'}
]

# Função que carrega e toca o som do arquivo especificado
def tocar_som(endereco):
    nota = pygame.mixer.Sound(endereco)  # Carrega o arquivo de áudio
    nota.play()  # Reproduz o som

# Função que é acionada quando uma tecla do teclado é pressionada
def tecla_pressionada(event):
    tecla = event.keysym  # Captura a tecla pressionada
    # Verifica se a tecla corresponde a um botão criado e se ainda não está ativada
    if tecla in botoes_associados and tecla not in teclas_ativas:
        teclas_ativas.add(tecla)  # Marca a tecla como ativa para evitar repetição
        btn = botoes_associados[tecla]  # Obtém o botão associado à tecla
        btn.config(relief='sunken')  # Altera a aparência para parecer pressionado
        btn.config(bg='#d8c2ff')  # Muda a cor para indicar tecla ativa
        # Busca o arquivo de som correspondente e toca a nota
        for letra in info_teclas_brancas:
            if tecla in letra['tecla']:
                tocar_som(letra['som'])

# Função que é acionada quando uma tecla do teclado é liberada (solta)
def tecla_liberada(event):
    tecla = event.keysym  # Captura a tecla liberada
    if tecla in botoes_associados:
        teclas_ativas.discard(tecla)  # Remove a tecla da lista de ativas
        btn = botoes_associados[tecla]  # Obtém o botão associado
        btn.config(relief='raised')  # Restaura a aparência original do botão
        btn.config(background='white')  # Restaura a cor original do botão

# Inicialização dos módulos do pygame para áudio
pygame.init()
pygame.mixer.init()

janela = tk.Tk()  # Cria a janela principal
janela.title('Piano Simples')  # Define o título da janela

teclas_ativas = set()  # Conjunto para controlar teclas pressionadas
botoes_associados = {}  # Dicionário que associa cada tecla do teclado ao botão correspondente

# Criação dos botões para cada nota e associação com teclas físicas
for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(
        janela,
        text=item['tecla'],        # Texto exibido no botão (ex: 'z')
        font=('Arial', 12),        # Fonte e tamanho do texto
        width=5,                   # Largura do botão
        height=9,                  # Altura do botão para simular tecla de piano
        background='white',        # Cor de fundo branca
        bd=4,                     # Largura da borda
        relief='raised',           # Estilo da borda (levantada)
        anchor=tk.S,               # Alinha o texto na parte inferior do botão
        command=lambda n=str(item['som']): tocar_som(n)  # Toca o som ao clicar no botão
    )
    botao.grid(row=0, column=posicao)  # Posiciona o botão na linha 0 e coluna conforme posição
    for t in item['tecla']:
        botoes_associados[t] = botao  # Mapeia a tecla física para o botão

# Liga os eventos de pressionar e soltar teclas para as funções correspondentes
janela.bind_all('<KeyPress>', tecla_pressionada)  # Detecta quando uma tecla é pressionada
janela.bind_all('<KeyRelease>', tecla_liberada)  # Detecta quando uma tecla é solta

janela.mainloop()  # Inicia o loop principal da interface gráfica
