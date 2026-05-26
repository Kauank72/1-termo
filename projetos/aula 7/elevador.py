# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O  para o andar ondelevador deve se movere a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas n/
# (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

print ("Bem-Vindo ao predio GORDINHO")
opcao = input("Qual andar você deseja ir?:")
andar_atual = 0
while True:
    try:
        destino = int(input("digite o andar de destino (0-10): "))
        if destino < 0 or destino > 10:
            raise ValueError("Andar inválido. por favor, dígite um número entre 0 e 10." )
        
        print(f"Elevador se movendo do andar {andar_atual} para o andar {destino}...")
        andar_atual = destino
        print(f"Chegamos ao andar {andar_atual}!")

        if input("Deseja escolher outro andar? (s/n): ").lower() != 's':
            print("Obrigado por usar o elevador! Até a próxima!")
            break
        for listagem in range(10):
            print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'}")

    except ValueError as ve:
        print(f"Erro: {ve}. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
        print("Programa encerrado.")
        break         
