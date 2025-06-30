import tkinter as tk  # Biblioteca para criar a interface gráfica
import pygame  # Biblioteca para manipulação de áudio

# Lista que mapeia teclas físicas do teclado ('z', 'x', etc) aos arquivos de som correspondentes
info_teclas_brancas = [
    {'tecla': ['z'], 'som': 'notas/c1.wav'},
    {'tecla': ['x'], 'som': 'notas/d1.wav'},
    {'tecla': ['c'], 'som': 'notas/e1.wav'},
    {'tecla': ['v'], 'som': 'notas/f1.wav'},
    {'tecla': ['b'], 'som': 'notas/g1.wav'},
    {'tecla': ['n'], 'som': 'notas/a1.wav'},
    {'tecla': ['m'], 'som': 'notas/b1.wav'}
]

# Função que carrega todos os sons de uma vez, retornando um dicionário
# onde a chave é o caminho do arquivo e o valor é o objeto Sound carregado
def carregar_sons(lista):
    return {i['som']: pygame.mixer.Sound(i['som']) for i in lista}

# Função que toca um som a partir do endereço (caminho) fornecido
# Agora utiliza o cache de sons pré-carregados para evitar recarregamento a cada toque
def tocar_som(endereco):
    nota = sons_cache.get(endereco)  # Obtém o objeto Sound do cache
    if nota:
        nota.play()  # Toca o som

# Função que responde ao evento de tecla pressionada no teclado físico
def tecla_pressionada(event):
    tecla = event.keysym  # Captura o nome da tecla pressionada
    if tecla in botoes_associados and tecla not in teclas_ativas:
        teclas_ativas.add(tecla)  # Marca tecla como ativa para evitar múltiplas execuções
        btn = botoes_associados[tecla]  # Obtém o botão associado para alteração visual
        btn.config(relief='sunken')  # Efeito de tecla pressionada
        btn.config(bg='#d8c2ff')  # Cor alterada para indicar estado ativo
        for letra in info_teclas_brancas:
            if tecla in letra['tecla']:
                tocar_som(letra['som'])  # Toca a nota correspondente

# Função que responde ao evento de tecla liberada (solta)
def tecla_liberada(event):
    tecla = event.keysym  # Captura o nome da tecla liberada
    if tecla in botoes_associados:
        teclas_ativas.discard(tecla)  # Remove a tecla do conjunto de teclas ativas
        btn = botoes_associados[tecla]
        btn.config(relief='raised')  # Restaura o efeito visual original do botão
        btn.config(background='white')  # Restaura a cor original

# Inicialização do pygame e do mixer de áudio
pygame.init()
pygame.mixer.init()

# Configura o mixer para permitir múltiplos canais simultâneos de áudio (64 canais)
pygame.mixer.set_num_channels(64)

# Pré-carrega todos os sons e armazena no dicionário global 'sons_cache'
sons_cache = carregar_sons(info_teclas_brancas)

janela = tk.Tk()  # Cria a janela principal
janela.title('Piano Simples')  # Define o título da janela

teclas_ativas = set()  # Conjunto para controle das teclas atualmente pressionadas
botoes_associados = {}  # Dicionário para mapear teclas físicas aos botões gráficos correspondentes

# Cria os botões correspondentes às notas do piano e associa cada tecla a seu botão
for posicao, item in enumerate(info_teclas_brancas):
    botao = tk.Button(
        janela,
        text=item['tecla'],
        font=('Arial', 12),
        width=5,
        height=9,
        background='white',
        bd=4,
        relief='raised',
        anchor=tk.S,
        command=lambda n=str(item['som']): tocar_som(n)  # Permite tocar som ao clicar no botão
    )
    botao.grid(row=0, column=posicao)  # Posiciona o botão na linha 0 e coluna conforme a posição
    for t in item['tecla']:
        botoes_associados[t] = botao  # Associa a tecla física ao botão criado

# Associa eventos globais de pressionar e soltar tecla para as funções definidas
janela.bind_all('<KeyPress>', tecla_pressionada)
janela.bind_all('<KeyRelease>', tecla_liberada)

janela.mainloop()  # Inicia o loop principal da interface
