import tkinter as tk


def tocar_som():
    print('Nota tocada')


janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

botao_de_teste = tk.Button(janela, text='Tecla', command=tocar_som)
botao_de_teste.pack()

janela.mainloop()
