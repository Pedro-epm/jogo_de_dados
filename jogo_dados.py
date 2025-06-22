import random

menu = '''

[1] Jogar com outro jogador
[2] Jogar com CPU
[3] Mostrar placar
[4] Sair do jogo

'''

player1_vitorias = 0
player2_vitorias = 0
player_vitorias = 0
cpu_vitorias = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        rodadas = 10
        a = random.randint(1, 100)
        while rodadas > 0:
            tentativa = int(input("Player 1, adivinhe o número: "))
            if tentativa == a:
                player1_vitorias += 1
                print("🎉 O player1 venceu!")
                break
            elif tentativa < a:
                print("Muito baixo")
            else:
                print("Muito alto")

            tentativa2 = int(input("Player 2, adivinhe o número: "))
            if tentativa2 == a:
                player2_vitorias += 1
                print("🎉 O player2 venceu!")
                break
            elif tentativa2 < a:
                print("Muito baixo")
            else:
                print("Muito alto")

            rodadas -= 1
        else:
            print(f"Ninguém venceu! O número era {a}.")

    elif opcao == "2":
        rodadas = 10
        a = random.randint(1, 100)
        while rodadas > 0:
            tentativa = int(input("Player, adivinhe o número: "))
            if tentativa == a:
                player_vitorias += 1
                print("🎉 Player venceu!")
                break
            elif tentativa < a:
                print("Muito baixo")
            else:
                print("Muito alto")

            cpu_jogada = random.randint(1, 100)
            print(f"CPU tentou {cpu_jogada}")
            if cpu_jogada == a:
                cpu_vitorias += 1
                print("🤖 CPU venceu!")
                break
            elif cpu_jogada < a:
                print("CPU tentou um número muito baixo")
            else:
                print("CPU tentou um número muito alto")

            rodadas -= 1
        else:
            print(f"Ninguém venceu! O número era {a}.")

    elif opcao == "3":
        print("::::::::::::: PLACAR :::::::::::::")
        print(f"Player 1 vitórias: {player1_vitorias}")
        print(f"Player 2 vitórias: {player2_vitorias}")
        print(f"Player (vs CPU) vitórias: {player_vitorias}")
        print(f"CPU vitórias: {cpu_vitorias}")
        print(":::::::::::::::::::::::::::::::::::")

    elif opcao == "4":
        print("Saindo do jogo, até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")
