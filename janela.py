def testado():
    mund = 'Olá mundo, teste para janelas'
    texto_vazio['text'] = mund



from tkinter import *

janela = Tk()
janela.geometry('250x250')
janela.title('Programas')
texto = Label(janela, text='Clique no botão')
texto.grid(column=0, row=0, padx=80, pady=10)
botao = Button(janela, text='enviar', command=(testado))
botao.grid(column=0, row=1, padx=80, pady=10)
texto_vazio = Label(janela, text='')
texto_vazio.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()
