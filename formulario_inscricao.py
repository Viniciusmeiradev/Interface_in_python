import tkinter as tk
from tkinter import messagebox

def submit():
    #Dados de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    #Verifica qual radiobutton selecionado
    linguagem_preferida = linguagem_var.get()

    #Imprime os dados no console
    print('Nome: ', nome)
    print('Email: ', email)
    print('Linguagem Preferida: ', linguagem_preferida)

    #Mostra a caixa de mensagem com os dados
    messagebox.showinfo('Dados Submetidos', f'Nome: {nome}\nEmail: {email}\nLinguagem Preferida: {linguagem_preferida}')

#Janela principal
janela = tk.Tk()
janela.title('Formulário de Inscrição')

#Frame
frame = tk.Frame(janela)
frame.pack(padx='10', pady='10')

#Label para o campo nome
nome_label = tk.Label(frame, text='Nome: ')
nome_label.grid(row=0, column=0, sticky='e')

#Campo entrada nome
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

#Label para o campo email
email_label = tk.Label(frame, text='Email: ')
email_label.grid(row=1, column=0, sticky='e')

#Campo entrada email
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

#Variavel para armazenar a escolha da linguagem
linguagem_var = tk.StringVar(value='Python')

#Radio Python
python_radio = tk.Radiobutton(frame, text='Python', variable=linguagem_var, value='Python')
python_radio.grid(row=2, column=0)

#Radio java
java_radio = tk.Radiobutton(frame, text='Java', variable=linguagem_var, value='Java')
java_radio.grid(row=2, column=1)

submit_button = tk.Button(frame, text='Submeter', command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

janela.mainloop()
