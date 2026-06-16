# 1. Utilizar tomada de decisão para elaboração do algoritmo
# 2. Utilizar estruturas condicionais para executar instruções com base em uma
# condição
# 3. Criar estruturas de repetição para executar um conjunto de instruções várias
# vezes
# 4. Aplicar operadores lógicos para avaliar e combinar condições booleanas
# 5. Utilizar lógica de programação para a resolução de problemas

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Biblioteca")
janela.geometry("400x200")

def cadastrar_livro():              
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    
    if titulo and autor:
        messagebox.showinfo("Sucesso", f"Livro '{titulo}' de {autor} cadastrado com sucesso!")
        entry_titulo.delete(0, tk.END)
        entry_autor.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")     
label_titulo = tk.Label(janela, text="Título:")
label_titulo.grid(row=0, column=0, padx=10, pady=5)
entry_titulo = tk.Entry(janela)
entry_titulo.grid(row=0, column=1, padx=10, pady=5)
label_autor = tk.Label(janela, text="Autor:")               
label_autor.grid(row=1, column=0, padx=10, pady=5)              
entry_autor = tk.Entry(janela)
entry_autor.grid(row=1, column=1, padx=10, pady=5)
btn_cadastrar = tk.Button(janela, text="Cadastrar Livro", command=cadastrar_livro)
btn_cadastrar.grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()