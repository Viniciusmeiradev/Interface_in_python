import tkinter as tk
from tkinter import ttk

#Função de coleta e impressao
def submit():
    #Coletar dados do campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    #Imprime os dados no console
    print('Nome: ', nome)
    print('E-mail: ', email)


root = tk.Tk()                                  #Janela Grafica principal
root.title('Formulário de Inscrição')           #Titulo da janela
root.geometry("200x100")

#Frame com os Widgets
frame = tk.Frame(root)                          #frame da janela - A parte que o usuário digita
frame.pack(padx=10, pady=10)                    #Distancia da borda xy


#Widget titulo - nome e email do campo de entrada
nome_titulo  = tk.Label(frame, text="Nome")
nome_titulo.grid(column=0, row=0)

email_titulo = tk.Label(frame, text="Email")
email_titulo.grid(column=0,row=1)


#Campo de entrada para nome
nome_entry = tk.Entry(frame)                    #Entrar com os dados do nome no frame
nome_entry.grid(row=0, column=1)                #Posicionamento da caixa nome em grid - linha e coluna

#Campo de entrada para Email
email_entry = tk.Entry(frame)                    #Entrar com os dados do nome no frame
email_entry.grid(row=1, column=1)               #Posicionamento da caixa email em grid - linha e coluna

#Botao submissao
submit_button = tk.Button(frame, text='Salvar', command=submit)        #Dados do botão no frame
submit_button.grid(row=2, columnspan=2, pady=10)                       #Posicionamento - o pady serve para afastar das outras linhas

#Iniciar o loop
root.mainloop()
