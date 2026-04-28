# Clean Code - aula 6
# Para que usar?
# print("Clean code - Aula 6")
# Aula = 6
# print(f"Estamos na aula {aula} de Clean code")
# ----------------------------------//------------------------
# Manipulação de arquivos e Texto
# texto ="  Python é Muito legal!  "
# print(texto.strip().upper())
# print(texto.strip().lower())
# print(texto.strip().capitalize())
# print(texto.strip().title())
# print(texto.strip().replace(" ", "_"))
# print(texto.strip().split())
# --------------------------------------//-----------------------------------
# # Escrevendo
# with open("notas.txt", "w") as arquivos:
#     arquivos.write("Estudar python hoje!")
#     arquivos.write("\nLer sobre Clean Code.")

# # Lendo
# with open("notas.txt", "r") as arquivos:
#     conteudo = arquivos.read()
#     print(conteudo)

# -----------------------------------//--------------------------------

# Exercicio 1
# Crie um programa que peça ao usuario para inserir uma frase e,
# em seguida, exiba a frase com as segintes transformaçoes:
# - Remova os espaços extras no inicio e no final da frase

# texto = input("digite uma frase: ")
# print(texto.strip().capitalize())
# ----------------------------------------/-------------------------------

# Exemplo 1
# crie um programa que leia o conteudo de um arquivo de texto e 
# conte quantas vezes a palavra "python" aparece no arquivo. Exiba
# o resultado para o usuario.

# print("Contagem de palavras em arquivos")
# with open("notas.txt", "r") as arquivos:
#     conteudo = arquivos.read()
#     contagem = conteudo.count("python")
#     print(f"A contagem de palavras {contagem} é de...")

# -----------------------------------//----------------------------
# Execução de comandos do sistemas
# import os #importa o módulo os para interagir com o sistema operacionais
# Onde estou?
# print(os.getcwd())

# Lista arquivos na pasta
# print(os.listdir())
# print(os.listdir(".."))
# print(os.listdir("..\\.."))
# print(os.listdir("C:\\Users"))
# print(os.listdir("C:\\Users\\Publico"))

#Outros comandos úteis:
#Criar pasta
# os.mkdir("nova_pasta")
#Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# #Excluir pasta
# os.rmdir("pasta_renomeada")
# ---------------------------//------------------------

# Exercicio 2
# crie um script que mostre o caminho da pasta atual.
# print(os.getcwd())
# ----------------------------//------------------------------------
# Exercícios 3
# Liste os arquivos da pasta atual
# print(os.listdir())
# -----------------------------//-----------------------------
# Exercícios 4
# Crie uma pasta chamada "projetos" e depois renomeia para 
# "meus_projetos". Por fim, exclua a pasta

# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")
# ----------------------------------//-------------------------

# Exercícios 5
# Crie um arquivo chamada "log.txt" e esceva a mensagem "log de atividades".
# Depois, leia o conteudo do arquivo e exiba na tela

# with open("log.txt", "w") as arquivos:
#     arquivos.write("log de atividades!")
# with open("log.txt", "r") as arquivos:
#     conteudo = arquivos.read()
#     print(conteudo)
# ------------------------------------//-------------------------------
# Exemplo de dicionario:
# Cria um dicionario com informacoes sobre uma pessoa e acessa um valor usado uma chave

# pessoa = {
#     "nome": "Aline",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "profissão": "Engenheira"
# }
# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "São Paulo",
#     "profissão": "Designer"
# }
# print(pessoa["cidade"]), pessoa["profissão"]
# print(pessoa2["nome"], pessoa["idade"], pessoa["profissão"])
# ------------------------------//---------------------------------------
# Exemplo 2 Desligar o pc (comando para windows)
# with open("desliga.bat", "w") as desligar:
#     desligar.write("shutdow -s -t  -c \ "Desligamento programa para daqui a 1 hora. salve seu trabalho!\"")