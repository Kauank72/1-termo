
# exercicio 1


# for sensor in range(1,11):
#     if sensor == 5:
#      print(f"Sensor n°{sensor}com falha")
#     print(f"Sonsor {sensor} sem falha")
#     continue
# print("Fim! :)")

# exercicio 2
# simule um semafaro com parada para cada cor. Determine um tempo que 
# deseja para que quando mudar para tal cor ele representa uma pausa 
# para cada cor. Use o continnue para pular a cor amarela (simulando um semáfaro
# com defeito que nao acente a luz amarelo)
import time
cores = ["verde, amarelo", "vermelho",]

for cor in cores:
   if cor == "Amarelo":
      print(f"Semáforo com defeito, pulando a cor {cor}...")
      continue # Pula a cor amarela
   print(f"Semáforo na cor {cor}. Parando por 3 segundos...")
   time.sleep(3) # Simula a pausa para cada cor
   print("fim do ciclo do semáforo.")

# exercicios 3
# uma fabrica tem 5 maquinas. peca ao usuario (via input dentro do loop)
# o consume em kwh de cada uma das 5 maquinas. Ao final do loop, o progama
# deve exibir o consumo total da fabrica.

# total_consumo = 0
# for maquina in range(1,6):
#     consumo = float(input(f"Digite o consume em kwh da máquina {maquina}: "))
#     total_consumo += consumo # Aculo o consumo total
# print(f"O consumo total da fábrica é de {total_consumo} kwh")

# exercicio 4 
# percorra uma lista de qualidade de medidas de pecas:
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# o patrao de qualidade aceita apenas pecas com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peca, diga s ela esta 
# "aprovada" "rejeitada".

# peca = {50.1, 49.8, 52.0, 50.0, 48.5}
# for medida in peca:
#     if medida >= 50.0:
#         print(f"Peça com medida {medida}mm: Aprovado")
#     else:
#         print(f"Peça com medida {medida}mm: Rejeitado")
# print("Fim da avaliação de peças. ")

# exercicio 5
# Uma balança indusrial esta pesandoum lote de 6 sacos de insumos.
# O peso ideal de cada saco é 50kg, mas o sistemas aceita vaiaçoes
# #crie um progama que peça ao usuario o peso de cada saco (via input dentro do loop)
# e,para cada um, informe se ele esta "dentro do limite"
# entre 48kg e 52kg ou fora do limie. No final, exiba quantos sacos estao dentro do liite.

# sacos_dl = 0 
# for saco in range(1,7):
#     peso = float(input(f"Digite o peso do saco {saco} em kg: "))
#     if 48 <= peso <=52:
#         print(f"Saco {saco} com peso {peso}kg: Dentro do limite")
#         sacos_dl += 1 # contra os sacos dentro do limite
#     else:
#         print(f"saco {saco} com peso {peso}kg: fora do limite")
# print(f"Quantidade de sacos dentro do limite: {sacos_dl}")

# dasafio: gestao de ciclo termico
# Você deve criar um progama que monitora a temperatura de uma estufa
# que processo um lote de 5 pecas.

# Regras do sistemas:
# o processo deve rodar em um loop ate que 5 peças validas sejam
# processadas.
# Para cada peça, peça ao usuario a temperatura atual (input).
# filtro de erro (continue): Se o usuario digitar uma temperatura
# negativa, exiba "erro de leitura no sensor" e use o continue para pedir a 
# temperatura novamente (essa leitura nao contra como peça processada).
# Parada de emergencia (break): Se a temperatura for maior que 150°C, o 
# sistema deve exibir "Alerta critico: risco de explosao!", interromper o
# loop imediatemente e encerrar o programa.


# ciclo = 0 
# while ciclo < 5:
#      temperatura = float(input(f"Digite a temperatura da peça {ciclo + 1} em °C:"))

#      if temperatura < 0:
#           print("Erro de leitura no sensor. Por favor, dígite uma temperatura válida")
#           continue # pede a temperatura novamente sem contar como peça processada
     
#      if temperatura > 150:
#           print("ALERTA CRÍTICO: risco de EXPLOSÃO!")
#           break # Interrrompe o loop imediatamente e encerre o progama
     
#      print(f"Peça {ciclo + 1} processada com temperatura {temperatura}°C.")
#      ciclo += 1 # Conta a peça processada

#      print(f"Peça {ciclo} processada com temperatura com sucesso. Temperatura dentro do limite.")
# print("Fim do monitoriamento de temperatura.")

# exercios 6 - Contrador de peças com falha (while + continue)
# Uma linha de producao tem um sensor que detecta falhas em peças. O 
# progam deve contar quantas pecas com falhas foram detectadas. o usuario
#  deve digitar "sim" para indicar que uma peca tem falha e "nao" para indicar que esta boa.
# O progama deve continuar pedindo a condicao da peça ate que o usuario digite "fim"
# no final, exiba o tatal de peças com falhas detectadas