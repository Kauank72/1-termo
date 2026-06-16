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
# 4.Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("400x250")

# def calcular_media():
#     nota1 = entrada_nota1.get()
#     nota2 = entrada_nota2.get()
#     nota3 = entrada_nota3.get()

#     if nota1 == "" or nota2 == "" or nota3 == "":
#         messagebox.showwarning("Aviso", "Digite as 3 notas!")
#         return

#     try:
#         nota1 = float(nota1)
#         nota2 = float(nota2)
#         nota3 = float(nota3)

#         media = (nota1 + nota2 + nota3) / 3

#         resultado.config(text=f"Média: {media:.2f}")

#     except ValueError:
#         messagebox.showerror("Erro", "Digite apenas números!")

# tk.Label(janela, text="Nota 1:").grid(row=0, column=0, padx=10, pady=10)
# tk.Label(janela, text="Nota 2:").grid(row=1, column=0, padx=10, pady=10)
# tk.Label(janela, text="Nota 3:").grid(row=2, column=0, padx=10, pady=10)

# entrada_nota1 = tk.Entry(janela)
# entrada_nota1.grid(row=0, column=1)

# entrada_nota2 = tk.Entry(janela)
# entrada_nota2.grid(row=1, column=1)

# entrada_nota3 = tk.Entry(janela)
# entrada_nota3.grid(row=2, column=1)


# btn_calcular = tk.Button(janela, text="Calcular Média", command=calcular_media)
# btn_calcular.grid(row=3, column=0, columnspan=2, pady=15)

# resultado = tk.Label(janela, text="")
# resultado.grid(row=4, column=0, columnspan=2)

# janela.mainloop()

# -------------------------------------------------------------------------------------
# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Termostato Inteligente")
# janela.geometry("400x250")

# def verificar_temperatura():
#     try:
#         temperatura = float(entrada_temperatura.get())

#         if temperatura < 40:
#             messagebox.showinfo("Termostato", "Baixa carga")
#         elif 40 <= temperatura <= 70:
#             messagebox.showinfo("Termostato", "Normal")
#         else:
#             messagebox.showwarning("Termostato", "ALERTA: Resfriamento Ativado!")

#     except ValueError:
#         messagebox.showerror("Erro", "Digite apenas números!")

# tk.Label(janela, text="Temperatura (°C):").grid(row=0, column=0, padx=10, pady=10)
# entrada_temperatura = tk.Entry(janela)
# entrada_temperatura.grid(row=0, column=1, padx=10, pady=10)

# btn_verificar = tk.Button(janela, text="Verificar", command=verificar_temperatura)
# btn_verificar.grid(row=1, column=0, columnspan=2, pady=15)

# janela.mainloop()

# --------------------------------------------------------------
# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("400x250")

# def classificar_lote():
#     codigo = entrada_codigo.get()

#     if codigo.startswith("A"):
#         messagebox.showinfo("Classificador de Lotes", "Alimentos")
#     elif codigo.startswith("E"):
#         messagebox.showinfo("Classificador de Lotes", "Eletrônicos")
#     else:
#         messagebox.showinfo("Classificador de Lotes", "Desconhecido")

# tk.Label(janela, text="Código do Produto:").grid(row=0, column=0, padx=10, pady=10)
# entrada_codigo = tk.Entry(janela)
# entrada_codigo.grid(row=0, column=1, padx=10, pady=10)

# btn_classificar = tk.Button(janela, text="Classificar", command=classificar_lote)
# btn_classificar.grid(row=1, column=0, columnspan=2, pady=15)

# janela.mainloop()

# ---------------------------------------------------------------------------------------

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Segurança de Operação")
# janela.geometry("400x250")
# def verificar_seguranca():      
#     sensor_porta = entrada_sensor.get().lower()
#     botao_emergencia = entrada_botao.get().lower()

#     if sensor_porta == "fechada" and botao_emergencia == "desligado":
#         messagebox.showinfo("Segurança de Operação", "Máquina pode iniciar!")
#     else:
#         messagebox.showwarning("Segurança de Operação", "Máquina NÃO pode iniciar!")        
# tk.Label(janela, text="Sensor da Porta (fechada/aberta):").grid(row=0, column=0, padx=10, pady=10)          
# entrada_sensor = tk.Entry(janela)         
# entrada_sensor.grid(row=0, column=1, padx=10, pady=10)            
# tk.Label(janela, text="Botão de Emergência (desligado/ligado):").grid(row=1, column=0, padx=10, pady=10)          
# entrada_botao = tk.Entry(janela)                              
# entrada_botao.grid(row=1, column=1, padx=10, pady=10)
# btn_verificar = tk.Button(janela, text="Verificar Segurança", command=verificar_seguranca)                          
# btn_verificar.grid(row=2, column=0, columnspan=2, pady=15)

# janela.mainloop()


# ----------------------------------------------------------------------------------------
# 8 Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Cálculo de Descarte") 
# janela.geometry("400x250")

# def calcular_descarte():
#     try:
#         total_peças = int(entrada_total.get())
#         defeituosas = int(entrada_defeituosas.get())

#         percentual_descarte = (defeituosas / total_peças) * 100

#         if percentual_descarte > 5:
#             messagebox.showwarning("Cálculo de Descarte", "Revisar Processo")
#         else:
#             messagebox.showinfo("Cálculo de Descarte", "Processo Otimizado")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite apenas números!")
# tk.Label(janela, text="Total de Peças:").grid(row=0, column=0, padx=10, pady=10)
# entrada_total = tk.Entry(janela)
# entrada_total.grid(row=0, column=1, padx=10, pady=10)
# tk.Label(janela, text="Peças Defeituosas:").grid(row=1, column=0, padx=10, pady=10)   
# entrada_defeituosas = tk.Entry(janela)
# entrada_defeituosas.grid(row=1, column=1, padx=10, pady=10) 

# btn_classificar = tk.Button(janela, text="Calcular Descarte", command=calcular_descarte)
# btn_classificar.grid(row=2, column=1, columnspan=2, pady=10)

# janela.mainloop()

# ---------------------------------------------------------------------------------------------------

# 9. Validção de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("validação de medida")   
# janela.geometry("400x250")

# def validar_medida():               


#     try:
#         medida = float(entrada_medida.get())

#         if 9.8 <= medida <= 10.2:
#             messagebox.showinfo("Validação de Medida", "Dentro da Tolerância")
#         elif medida < 9.8:
#             messagebox.showwarning("Validação de Medida", "Abaixo da Tolerância")
#         else:
#             messagebox.showwarning("Validação de Medida", "Acima da Tolerância")

#     except ValueError:
#         messagebox.showerror("Erro", "Digite apenas números!")                         

# tk.Label(janela, text="Medida (mm):").grid(row=0, column=0, padx=10, pady=10)
# entrada_medida = tk.Entry(janela)
# entrada_medida.grid(row=0, column=1, padx=10, pady=10)

# btn_validar = tk.Button(janela, text="Validar Medida", command=validar_medida)
# btn_validar.grid(row=1, column=0, columnspan=2, pady=10)

# janela.mainloop()

# ----------------------------------------------------------------------------------------------------

# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Contagem Regressiva de Setup")   
# janela.geometry("400x250")

# def contagem_regressiva():
#     for i in range(10, 0, -1):
#         messagebox.showinfo("Contagem Regressiva", f"{i}")
#     messagebox.showinfo("Contagem Regressiva", "Prensa Ativada!")

# btn_iniciar = tk.Button(janela, text="Iniciar Setup", command=contagem_regressiva)
# btn_iniciar.grid(row=0, column=0, columnspan=2, pady=10)

# janela.mainloop()
