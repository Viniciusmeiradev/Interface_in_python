import psycopg2 import Error
from faker import Faker
import tkinter as tk
from tkinter import tkk



#Codigo CRUD completo para nome e preco de um produto


#Criar conexao
conexao = psycopg2.connect(database = "PostgresDB", user='admin', password="admin123", host="127.0.0.1", port="5432")
print("Conexao com o banco de dados aberta com sucesso!")

#Criacao do cursor
meu_cursor = conexao.cursor()

if __name__=='__main__':
    #Criacao da tabela
    meu_cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUTO(
                        CODIGO SERIAL PRIMARY KEY,
                        NOME VARCHAR(30) NOT NULL,
                        PRECO NUMERIC(10, 2) NOT NULL);""")

conexao.commit()
print("Tabela Criada Com Sucesso!")
conexao.close()



#Criação do arquivo banco de dados
class AppBD:

    #Objeto que vai armazenar o cursor
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()                        #conexao
    #Cursor que vai ser armazenado no objeto

    def connect_to_db(self):
        self.conn = conexao                         #Realiza a conexao
        self.cur = meu_cursor                       #Realiza o cursor
        print("Conexao com o Banco de Dados aberta com sucesso!")


    def selecionar_dados(self):
        try:
            self.cur.execute("SELECT * FROM PRODUTO ORDER BY CODIGO")               #Faz uma lista dos dados
            registros = self.cur.fetchall()
            return registros
        except(Exception, Error) as error:
            print("Erro ao selecionar dados", error)
            return []


    def inserir_dados(self, nome, preco):
        try:
            self.cur.execute(""" INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)""", (nome,preco))
            self.conn.commit()
            print("Inserção realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao inserir dados", error)


    def atualizar_dados(self, codigo, nome, preco):
        try:
            self.cur.execute("""UPDATE PRODUTO SET NOME=%s, PRECO = %s,WHERE CODIGO = %s """,(nome, preco, codigo))
            self.conn.commit()
            print("Atualização realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao atualizar dados", error)


    def excluir_dados(self, codigo):
        try:
            self.cur.execute("""DELETE FROM PRODUTO WHERE CODIGO = %s""", (codigo,))
            self.conn.commit()
            print("Exclusão realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao excluir dados", error)

if __name__=='__main__':
    app_bd= AppBD()
    fake = Faker("pt_BR")

    for _ in range(10):
        nome = fake.word()
        preco = round(fake.random_number(digits=5) / 100, 2)
        app_bd.inserir_dados(nome, preco)
        print(nome, preco)





#CODIGO DA INTERFACE DO PROGRAMA - GUI

class PrincipalBD:
    def __init__(self, root,db):
        self.root = root
        self.db = db
        self.root.title("Gestão de Produtos")

        #Componentes da interface gráfica

        #Componente da entrada id
        self.lblCodigo = tk.Label(root, text="Código")
        self.lblCodigo.grid(row=0, column=0)
        self.txtCodigo = tk.Entry(root)
        self.txtCodigo.grid(row=0, column=1)

        #Componente entrada nome
        self.lblNome = tk.Label(root, text="Nome")
        self.lblNome.grid(row=1, column=0)
        self.lblNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        #Componente entrada preco
        self.lblPreco = tk.Label(root, text="Preço")
        self.lblPreco.grid(row=2, column=0)
        self.txtPreco = tk.Entry(root)
        self.txtPreco.grid(row=2, column=1)

        #Botoes
        self.btnCadastrar = tk.Button(root, text="Cadastrar", command=self.fCadastrarProduto)           #Botao de cadastrar
        self.btnCadastrar.grid(row=3, column=0)

        self.btnAtualizar = tk.Button(root, text="Atualizar", command=self.fAtualizarProduto)           #Botao de atualizar
        self.btnAtualizar.grid(row=3, column=1)

        self.btnExcluir = tk.Button(root, text="Excluir", command=self.fExcluirProduto)                 #Botao de Excluir
        self.btnExcluir.grid(row=4, column=0)

        self.btnLimpar = tk.Button(root, text="Limpar", command=self.fLimparTela)                       #Botao de Limpar
        self.btnLimpar.grid(row=4, column=1)

        self.tree = ttk.Treeview(root, columns=("CODIGO", "NOME", "PRECO"), show='headings')
        self.tree.heading("CODIGO", text="Código")
        self.tree.heading("NOME", text="Nome")
        self.tree.heading("PRECO", text="Preço")
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.bind("<ButtonRelease-1>", self.apresentarRegistrosSelecionados)

        self.carregarDadosIniciais()

    def fCadastrarProduto(self):
        codigo = self.txtCodigo.get()
        nome=self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.inserir_dados(nome, preco)
        self.tree.insert("", "end", values=(codigo, nome, preco))
        self.fLimparTela()

    def fAtualizarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.atualizar_dados(codigo, nome, preco)
        self.fLimparTela()
        self.carregarDadosIniciais()

    def fExcluirProduto(self):
        codigo = self.txtCodigo.get()
        self.db.excluir_dados(codigo)
        self.fLimparTela()
        self.carregarDadosIniciais()

    def fLimparTela(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)

    def apresentarRegistrosSelecionados(self, event):
        item = self.tree.selection()[0]
        valores = self.tree.item(item, "values")
        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.insert(tk.END, valores[0])
        self.txtNome.delete(0, tk.END)
        self.txtNome.insert(tk.END, valores[1])
        self.txtPreco.delete(0, tk.END)
        self.txtPreco.insert(tk.END, valores[2])

    def carregarDadosIniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        registros = self.db.selecionar_dados()
        for registro in registros:
            self.tree.insert("", "end", values=registro)

#Criando a interface gráfica
root = tk.Tk()
app_bd = AppBD
app_gui = PrincipalBD(root, app_bd)
root.mainloop()
