  1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
 jogador [nick] está no nível [nível] e pronto para a partida!"

 nome = input("digite o seu nick")
# nivel = input("seu nivel atual")

 print(f"jogador {nome} está no nível {nivel} e pronto para a partida!")
 -------------------------------------------/-----------------------------------
 Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
 multiplique por 4 para mostrar quanto ele terá no final do mês.

 valor_da_mesada = int(input("qual o valor da sua mesada por semana?"))
 valor_final = valor_da_mesada * 4
 -----------------------------------/---------------------------------------------
 print(f"voce tera no final do mes  {valor_final}: ")

 Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
 Megabytes (MB) (multiplique por 1024).

 valor_Gigabytes = int(input("fala um valor em gigabytes: "))
 conversao_em_Megabytes = valor_Gigabytes * 1024

 print(f"sua conversao de Gigabytes para Megabytes sera :{conversao_em_Megabytes} ")

 ------------------------------------/-----------------------------------------------
 Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
 média final.

 media_da_nota1 = int(input("digite a sua nota de portuques: "))
 media_da_nota2 = int(input("digite a sua nota de matematica: "))

 somativa = media_da_nota1 + media_da_nota2
 media_final = somativa / 2

 print(f"sua nota de portuques é: {media_final} ")
 print(f"sua nota de matematica é: {media_final} ")

 -----------------------------------/---------------------

 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
 o aluno ganhou hoje. Exiba o total atualizado.


 seguidores_atuais = int(input("digite a quantidades de seguidores atuais: "))
 novos_seguidores = int(input("quantos seguidores voce ganhou hoje?"))
 somativa = seguidores_atuais + novos_seguidores

 print(f"voce tem {somativa} seguidores :")
 --------------------------------/----------------------------

 Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
 ele já viveu (idade * 365).

 idade = int(input("qual é a sua idade?"))

 idade_final = idade * 365

 print(f"voce ja esta vivo a : {idade_final}")
 --------------------------------/---------------------------

 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
 total da conta.

 salgado = int(input("qual o peco do salgado?"))
 suco = int(input("qual o preco do suco?"))

 somativa = salgado + suco

 print(f"A sua compra ficou no valor de: {somativa}")
 -----------------------------/---------------------------

 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
 em que ele nasceu.

 ano_atual = int(input("qual e o ano atual?"))
 idade_do_aluno = int(input("qual a idade do aluno?"))

 calculo = ano_atual - idade_do_aluno

 print(f"O ano que o aluno naceu é: {calculo} ")
 ----------------------------/---------------------

 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
 "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
 mais, "Acesso liberado".

 idade = int(input("qual é a sua idade?"))

if idade  < 13:
    print("Acesso restrito")
elif idade < 17:
    print("Acesso moderado")
else:
    print("Acesso liberado")

    -----------------------------/----------------------------------

10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
chegar em 10 e exibe: "Por favor, conecte o carregador!".

bateria = 100

while bateria > 10:
    print(f"bateria em {bateria}%")
    bateria -= 10

    print(f"Por favor, conecte o carregador: {bateria}")

11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".

 limite = int(input("Digite o limite de curtidas: "))

for i in range(1, limite + 1):

    print(f"curtida n° {i} recebida!")
-----------------------------------/-----------------------------

12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
 aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
 quantas vezes ele adiciona itens ao carrinho (use um contador).

contador_itens = 0

while True:
    produto = input("digite o nome do produto (ou 'sair' para finalizar): ")

    if produto.lower() == "sair":
       break
    
    if produto.strip() == "":
        continue

    contador_itens += 1
    print(f"{produto} adicionado com sucesso!")