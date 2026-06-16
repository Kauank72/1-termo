# Criar um algoritmo para que:

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

print("Bem-vindo ao shooping")

print("1 - Emitir Ticket")
print("2 - Verificar TAG")
print("3 - Interfone")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print("Emitindo ticket...")

    placa = input("Digite a placa: ")
    entrada = float(input("Hora de entrada: "))
    saida = float(input("Hora de saída: "))
    valor_hora = float(input("Valor por hora: "))

    tempo = saida - entrada
    total = tempo * valor_hora

    print(f"Tempo no estacionamento: {tempo} horas")
    print(f"Valor total: R${total:.2f}")

elif opcao == 2:
    print("Verificando TAG...")
    print("Cobrança será feita na fatura da TAG")

elif opcao == 3:
    print("Acesso liberado pelo interfone")

else:
    print("Opção inválida")

print("Obrigado por utilizar nosso serviço!")
