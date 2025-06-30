import tkinter as tk

janela = tk.Tk()
janela.title('Piano Simples')
janela.geometry('300x200')

botao_de_teste = tk.Button(janela, text='Tecla')
botao_de_teste.pack()

janela.mainloop()
