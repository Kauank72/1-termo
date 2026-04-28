# 1. o laço 'for' (repetições determinadas)
# use o 'for' quando você sabe exatamente quantas vezes algo deve contecer (como ler 10 sensores ou processar uma lista de peças).
# exemplo: relatorio de producao diaria 
# imagina que voce tem uma meta de produzir 5 lotes e quer numerar cada um:

# exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Quantidade verificada. [OK]")
#     print("Produção do dia finalizada!")

# #exemplo 2
# for b in range(10):
#    print(f"quantidade total {b} foi...")

# #exemplo 3 
# # imagine o seguinte cenario, iremos produzir 20 disco de vínil

# for disco in range(1, 21):
#     print(f"quantidade de disco produzido {disco} foi...")
#     print("producao do dia finalizada!")

# #exenplo 4
# pecas = ["engrenagens", "eixo", "rolamento", "parafuso", "maretelo","pregos", "chave de fenda"]
# itempecas = ["cilindricas", "eixo conico", "radiais", "madeiras", "bola", "cabeca chta", "chave verde"]


# for item in pecas:
#     print(f"item em estoque: {item} e {itempecas}")
#     for item2 in itempecas:
#         print(f"item de pecas em estoque: {itempecas}")


#exemplo 5
#imagine a seguir situacao gostaria de ter um menu onde pudesse perguntar qual opcao voce deseja e a  partir da selecao ele listra os produtos

# print("loja do fortin lombas com leo lombas e gordin lombas")
# print("opcao 1- pecas")
# print("opcao 2- item pecas")
# menu = int(input("escolha uma opcao"))

# pecas = ["engrenagens", "eixo", "rolamento", "parafuso", "maretelo","pregos", "chave de fenda"]
# itempecas = ["cilindricas", "eixo conico", "radiais", "madeiras", "bola", "cabeca chta", "chave verde"]

# if menu == 1:
#     for item1 in pecas:
#         print(f"sua lista de pecas {pecas} sao...")
# elif menu == 2:
#         print(f"sua lista de item de pecas {itempecas} sao...")
# else:
#     print("opcao ivalida: encerrando o sistema")        
     

# #exercio 1
# for ciclo in range(1, 11):
#  print(f"peca n {ciclo} foi...")
# print("ciclo de producao concluido")

#exercios 2

# frutas = ["banana", "manga", "melancia", "abacaxi",]
# frutasfeiras = ["10", "5", "10", "13",]

# for banana in range(1,11):
#    print(f"item em estoque: {banana}")

# for manga in range(1,6):
#    print(f"item em estoque: {manga}")

# for melancia in range(1,11):
#    print(f"item em estoque: {melancia}")
   
# for abacaxi in range(1,14):
#    print(f"item em estoque: {abacaxi}")
   
# total_banana = 10
# total_manga = 5 
# total_melancia = 10
# total_abacaxi = 13
            
# total_geral = total_banana + total_manga + total_melancia + total_abacaxi

# print(" A producao final foi: ", total_geral)

#Exercios 3
# print("qual tabuada voce deseja")
# numero1 = int(input("quero a tabuada do: "))

# print ("tabuada do numero: ")

# for numero2 in range(1, 11):
#     resultado = numero1 * numero2
#     print(f"{numero1} x {numero2} = {resultado}")