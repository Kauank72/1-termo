# lista de tempertura lidas pelos sensor por minuto

# Exemplo 1
# import time
# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3 # simulando aquecimento da máquina
# print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo 2 
# lista de temperaturas lidas pelo sensor por minuto

# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # o lobo para aqui e NÃO lê os próximos valores (85 80)
#     print(f"Temperatura está em {temp}°C. Operação normal.")

# print("Sistema desisligado. Aguardando manutenção")

# Exemplo 3

# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"AVISO: peça de {peca} detectado. Desviando para descarte...")
#         continue # Pula o restante do código abaixo e vai para a próxima peça
#     # Este código só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")

# print("Fim do lote de produção.")
