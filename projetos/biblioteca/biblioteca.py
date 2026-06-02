# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("biblioteca")
# janela.geometry("400x200")

# def janela_bemvindo():
#     Aluno = Aluno_usuario.get()
#     biblioteca = biblioteca_usuario.get()


#     if Aluno == "" and biblioteca == "":
#         messagebox.showwarning("Aviso", "Digite seu nome e o nome do livro")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Olá usuário, {Aluno}, seu livro escolhido foi: {biblioteca} - Seja bem-vindo a bibliotecaria")




# lbl_mensagem = tk.Label(janela, text="Digite seu nome")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_idade = tk.Label(janela, text="Digite o nome do livro ")
# lbl_idade.grid(row=1, column=0, pady=10, padx=10)


# Aluno_usuario = tk.Entry(janela, font=("Arial", 12))
# Aluno_usuario.grid(row=0, column=1, pady=10, padx=10)
# biblioteca_usuario = tk.Entry(janela, font=("Arial", 12))
# biblioteca_usuario.grid(row=1, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)


# janela.mainloop()

# -----------------------------------------------------
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Biblioteca")
janela.geometry("400x200")

def janela_bemvindo():
    aluno = Aluno_usuario.get()
    biblioteca = biblioteca_usuario.get()

    if aluno == "" or biblioteca == "":
        messagebox.showwarning("Aviso","Digite seu nome e o nome do livro")
    else:
        messagebox.showinfo(
            "Bem-Vindo",
            f"Olá, {aluno}!\n"
            f"Seu livro escolhido foi: {biblioteca}\n"
            f"Seja bem-vindo à biblioteca!" )

lbl_mensagem = tk.Label(janela, text="Digite seu nome")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

lbl_livro = tk.Label(janela, text="Digite o nome do livro")
lbl_livro.grid(row=1, column=0, pady=10, padx=10)

Aluno_usuario = tk.Entry(janela, font=("Arial", 12))
Aluno_usuario.grid(row=0, column=1, pady=10, padx=10)

biblioteca_usuario = tk.Entry(janela, font=("Arial", 12))
biblioteca_usuario.grid(row=1, column=1, pady=10, padx=10)

btn_mensagem = tk.Button(
    janela,
    text="Mensagem",
    command=janela_bemvindo
)
btn_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()



