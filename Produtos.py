import tkinter as tk
from tkinter import messagebox
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='python_sql'
    )

def criar_produto():
    nome_produto = entry_nome.get()
    valor = int(entry_valor.get())
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo("Sucesso", "Produto criado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar produto: {e}")
    finally:
        cursor.close()
        conexao.close()

def ler_produtos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        comando = 'SELECT nome_produto, valor FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        produtos = '\n'.join([f'Nome: {linha[0]} - Valor: {linha[1]}' for linha in resultado])
        
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, produtos)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler produtos: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_produto():
    nome_produto = entry_deletar.get()
    
    if nome_produto == "":
        messagebox.showwarning("Aviso", "Por favor, insira o nome do produto!")
        return
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit()
        
        if cursor.rowcount > 0:
            messagebox.showinfo("Sucesso", "Produto deletado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Produto não encontrado!")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao deletar produto: {e}")
    finally:
        cursor.close()
        conexao.close()

root = tk.Tk()
root.title("CRUD de Produtos")
root.geometry("400x700")
root.config(bg="#f4f4f9")

# Estilos
label_style = {"bg": "#f4f4f9", "font": ("Arial", 10, "bold")}
entry_style = {"width": 30, "font": ("Arial", 12)}

# Campos de criação de produto
label_nome = tk.Label(root, text="Nome do Produto:", **label_style)
label_nome.pack(pady=5)

entry_nome = tk.Entry(root, **entry_style)
entry_nome.pack(pady=5)

label_valor = tk.Label(root, text="Valor do Produto:", **label_style)
label_valor.pack(pady=5)

entry_valor = tk.Entry(root, **entry_style)
entry_valor.pack(pady=5)

botao_criar = tk.Button(root, text="Criar Produto", command=criar_produto, bg="#4CAF50", fg="white", font=("Arial", 12), relief="raised")
botao_criar.pack(pady=10)

botao_ler = tk.Button(root, text="Ler Produtos", command=ler_produtos, bg="#2196F3", fg="white", font=("Arial", 12), relief="raised")
botao_ler.pack(pady=10)

text_area = tk.Text(root, height=10, width=40, font=("Arial", 12))
text_area.pack(pady=10)

# Campos de deletar produto
label_deletar = tk.Label(root, text="Nome do Produto a Deletar:", **label_style)
label_deletar.pack(pady=5)

entry_deletar = tk.Entry(root, **entry_style)
entry_deletar.pack(pady=5)

botao_deletar = tk.Button(root, text="Deletar Produto", command=deletar_produto, bg="#f44336", fg="white", font=("Arial", 12), relief="raised")
botao_deletar.pack(pady=10)

root.mainloop()