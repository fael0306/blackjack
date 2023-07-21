import bblackjack as bb

def main():
    # Inicializa as mãos do jogador e do computador
    bb.inicializamao()
    bb.inicializamaopc()

    try:
        # Verifica se o jogador ganhou com Blackjack logo no início
        situacao = bb.testavitoriabj()

        # Se não ganhou, inicia o jogo
        while not situacao:
            # Mostra a mão do jogador
            bb.mostramao()

            # Pergunta ao jogador qual ação deseja tomar
            pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n"))

            if pergunta == 1:
                # O jogador escolheu puxar mais uma carta
                bb.puxacarta()

                # Se a soma das cartas do jogador ultrapassar 21, ele perde imediatamente
                if sum(bb.pontuacaodacarta) > 21:
                    print("\nVocê ultrapassou 21 pontos. Vitória do PC.")
                    break

            elif pergunta == 2:
                # O jogador escolheu encerrar a rodada, o computador joga e verifica o resultado
                if bb.pcjoga():
                    print("\nVocê perdeu! O PC fez Blackjack.")
                else:
                    print(f"\nO PC estourou com {sum(bb.pontuacaopc)} pontos.")
                    print("\nVocê venceu!")
                break

            elif pergunta == 3:
                # O jogador escolheu verificar a vitória
                if bb.testavitoriabj():
                    print("Você venceu por Blackjack.")
                elif bb.testavitoriapontos() and sum(bb.pontuacaopc) > 21:
                    print("\nParabéns. Você venceu! O PC estourou.")
                    print(f"\nResultado: {sum(bb.pontuacaodacarta)} x {sum(bb.pontuacaopc)}")
                elif bb.testavitoriapontos() and sum(bb.pontuacaopc) < 21:
                    print("\nParabéns. Você venceu por pontuação!")
                    print(f"\nResultado: {sum(bb.pontuacaodacarta)} x {sum(bb.pontuacaopc)}")
                else:
                    print("\nVocê perdeu!")
                break

        # Verifica se o jogador venceu por Blackjack após o loop
        if sum(bb.pontuacaodacarta) == 21:
            print("\nVocê venceu por Blackjack!")
        
        # Mostra as cartas do jogador e a pontuação final
        print("Cartas da sua mão:", ", ".join(map(str, bb.cartasmao)))
        print("Sua pontuação final: ", sum(bb.pontuacaodacarta))

        # Mostra as cartas do computador e a pontuação final do computador
        print("\nCartas da mão do PC:", ", ".join(map(str, bb.cartaspc)))
        print("Pontuação final do PC: ", sum(bb.pontuacaopc))

    except ValueError:
        print("\nO valor digitado é inválido")

if __name__ == "__main__":
    main()