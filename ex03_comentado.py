import tkinter as tk

janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

# Cria um botão chamado 'botao_de_teste'
# - Ele será exibido dentro da janela principal (janela)
# - O texto que aparece no botão será 'Tecla'
botao_de_teste = tk.Button(janela, text='Tecla')

# Exibe o botão na janela, usando o método pack() que posiciona automaticamente
botao_de_teste.pack()

janela.mainloop()
