# Exercícios de progamação Python: "o caça-Erros"

# 1. O Problema da Idade:

# idade = input("Dígite sua idade:")
# if idade >= 18:
#     print("Você é maior de idade.")
# --------------------------------------------------
# corrigido

# idade = int(input("Dígite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade.")
# -------------------------------------------------------
# # melhorado

# idade = int(input("Dígite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade")
# --------------------------------------------------------
# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda,nome!")
# -----------------------------------------
# corrigido
# nome = "mariana"
# print(f"seja bem -vinda, {nome}")
# --------------------------------------------
# melhorado
# nome = input("qual o seu nome? ")
# print(f"Seja bem-vindo, {nome}")
# ------------------------------------------------
# 3. Falta de Espaço

# numero = 10
# if numero > 5:
# print("O número é maior que cinco")
# else:
# print("O número é menor ou igual a cinco")
# -----------------------------------------------------

# corrigido
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco")
# else:
#     print(f"O número é menor ou igual a cinco")
    
# -------------------------------------------------------
# melhorado
# numero = float(input("qual o numero?"))
# if numero > 5:
#     print("o menuro é maior que cinco")
# elif numero == 5:
#     print("o numero é igual a cinco")
# else:
#     print("o numero é menor que cinco")
# ---------------------------------------------------------
# 4. Esquecimento Fatal

# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso")
# -------------------------------------------------------
# corrigido

# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso")
# ----------------------------------------------------------
# melhorado

# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso")
# else:
#     print("acesso negado")
# -------------------------------------------

# 5. Atribuição vs. Comparação

# clima = "ensolarado"
# if clima = "chuvoso":
#     print("Leve um gurda-chuva")
# -----------------------------------------------
# corrigido

# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um gurda-chuva")
# --------------------------------------------------

# melhorado

# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um gurda-chuva")
# elif clima == "ensolarado":
#     print("aproveite o sol")
# else:
#     print("o clima esta bom, nao precisa de guarda-chuva")
# ---------------------------------------

# 6. Misturando Alhos com Bugalhos

# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")
# ---------------------------------------------------
# corrigido

# pontos = 50
# print("Parabéns! Você fez ", pontos ," pontos.")
# ----------------------------------------------------
# melhorado

# pontos = 50
# print(f"Parabéns! Você fez " {pontos} " pontos.")
# ---------------------------------------------------------

# 7. A Ordem dos Fatores

# O sistema deve dar "Excelente" para notas 9 ou 10.

# nota = 9.5

# if nota >=7:
#     print("Aprovado")
# elif nota >=9:
#     print("Exelente!")
# ------------------------------------------------------
# corrigido

# nota = 9.5

# if nota >=9:
#     print("Exelente!")
# else:
#     print("Aprovado")
# ---------------------------------------------------
# melhorado

# nota = float(input("qual é a nota?"))
# if nota >=9:
#     print("Exelente!")
# elif nota +=6:
#     print("Aprovado")
# else:
#     print("Reprovado")
# ------------------------------------------------------

# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.

# for i in range(5):
# print(i)
# ---------------------------------------
# corrigido

# for i in range(5):
#     print(i)
# ------------------------------------------------
#  melhorado

# numero = int(input("Digite o número:  "))
# for i in range(numero):
#     print(i)

# ------------------------------------------------
# 9. O Loop Eterno

# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
# O código deveria parar após 3 tentativas
# ---------------------------------------------------
# corrido

# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas = tentativas + 1
# print("Fim das tentativas.")
# ------------------------------------------------
# melhorado
# for i in range(1, 4):
#     print(f"Tentativa {i}: Conectando...")

# print("Fim das tentativas.")
# -------------------------------------------------

# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"

# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# corrigido
# senha = ""
# while senha != "Phyton123":
#     senha = input("Digite sua senha secreta: ")

# print("Acesso Liberado!")
# ------------------------------------------------

# melhorado
# print("Seja Bem-Vindo ao gerenciador de senhas! \n Coloque senha e iremos ver se seu acesso é possível!")
# senha = ""
# while senha != "phyton123":
#     senha = input("digite sua senha secreta: ")

# print("Acesso liberado")
