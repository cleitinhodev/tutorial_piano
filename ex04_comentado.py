import tkinter as tk

# Define uma função chamada 'tocar_som'
# Essa função será chamada quando o botão for clicado
def tocar_som():
    print('Nota tocada')  # Exibe a mensagem no console (simulando tocar uma nota)

janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

# Cria um botão com o texto 'Tecla' e associa a função 'tocar_som' ao clique
botao_de_teste = tk.Button(janela, text='Tecla', command=tocar_som)

# Posiciona o botão na janela
botao_de_teste.pack()

janela.mainloop()
