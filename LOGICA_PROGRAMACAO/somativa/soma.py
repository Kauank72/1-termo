# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("400x200")


# def janela_bemvindo():
#     Nome = Nome_usuario.get()
#     turno = turno_usuario.get()


#     if Nome == "" and turno == "":
#         messagebox.showwarning("Aviso", "Digite seu nome e o turno")

#     else:
#         messagebox.showinfo("Bem-Vindo", f"Olá usuário, {Nome}, seu turno escolhido foi: {turno} - Seja bem-vindo")

# lbl_mensagem = tk.Label(janela, text="Digite seu nome")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_turno = tk.Label(janela, text="Digite o seu turno A, B e C")
# lbl_turno.grid(row=1, column=0, pady=10, padx=10)


# Nome_usuario = tk.Entry(janela, font=("Arial", 12))
# Nome_usuario.grid(row=0, column=1, pady=10, padx=10)
# turno_usuario = tk.Entry(janela, font=("Arial", 12))
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()
# ---------------------------------------------------------------------------------

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("calculo")
# janela.geometry("400x200")

# def janela_bemvindo():
#     peças = int(peças_usuario.get())
#     horas = int(horas_usuario.get())
    

#     if peças == "" and horas == "":
#         messagebox.showwarning("Aviso", "quandas horas?")
#     else:
#         producao_total = peças * 8
#         messagebox.showinfo("Bem-Vindo", f"quantidade de {peças} produzidas em 8  foi de: {producao_total}")


# lbl_mensagem = tk.Label(janela, text="Qual é a quantidades de peças produzidas em 1 hora")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_peças = tk.Label(janela, text="Digite a horas ")
# lbl_peças.grid(row=1, column=0, pady=10, padx=10)


# peças_usuario = tk.Entry(janela, font=("Arial", 12))
# peças_usuario.grid(row=0, column=1, pady=10, padx=10)
# horas_usuario = tk.Entry(janela, font=("Arial", 12))
# horas_usuario.grid(row=1, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)


# janela.mainloop()
# -------------------------------------------------------------------------------------
# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("conversor")
# janela.geometry("400x200")

# def janela_bemvindo():
#     Bar = int(Bar_usuario.get())
    
    

#     if Bar == "":
#         messagebox.showwarning("Aviso", "conversao")
#     else:
#         conversao_total = Bar *  14.5
#         messagebox.showinfo("Bem-Vindo", f"A conversao de {Bar} foi de: {conversao_total}")


# lbl_mensagem = tk.Label(janela, text="Qual a pressao do Bar")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)



# Bar_usuario = tk.Entry(janela, font=("Arial", 12))
# Bar_usuario.grid(row=0, column=1, pady=10, padx=10)



# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)


# janela.mainloop()
# ---------------------------------------------------------------------
4.Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
aritmética simples delas.

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("conversor")
janela.geometry("400x200")

def janela_bemvindo():
    nota1(nota_usuario.get())
    nota2(nota_usuario.get())
    nota3(nota_usuario.get())

if nota1 == "" and nota2 == "" and nota3 == "":
  messagebox.showwarning("Aviso", "digete a sua nota")
else:
    try:
       
       valor_notas = nota1 + nota2 + nota3
       











