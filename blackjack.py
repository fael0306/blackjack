import bblackjack as bb

def main():
    bb.inicializamao()
    bb.inicializamaopc()

    try:
        situacao = bb.testavitoriabj()

        if not situacao:
            bb.pcjoga()
            bb.mostramao()

        while not situacao:
            pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n"))

            if pergunta == 1:
                bb.puxacarta()
                situacao = bb.testavitoriabj()
                bb.mostramao()

            elif pergunta == 2:
                pc_venceu = bb.pcjoga()
                if pc_venceu:
                    print("\nVocê perdeu! O PC fez Blackjack.")
                    break
                else:
                    print(f"\nO PC estourou com {sum(bb.pontuacaopc)} pontos.")
                    print("\nVocê venceu!")
                    break

            elif pergunta == 3:
                if bb.testavitoriabj():
                    print("Você venceu por Blackjack.")
                elif bb.testavitoriapontos() and sum(bb.pontuacaopc)>21:
                    print("\nParabéns. Você venceu! O PC estourou.")
                    print(f"\nResultado: {sum(bb.pontuacaodacarta)} x {sum(bb.pontuacaopc)}")
                elif bb.testavitoriapontos() and sum(bb.pontuacaopc)<21:
                    print("\nParabéns. Você venceu por pontuação!")
                    print(f"\nResultado: {sum(bb.pontuacaodacarta)} x {sum(bb.pontuacaopc)}")
                elif not bb.testavitoriapontos():
                    print("\nVocê perdeu!")
                elif bb.testavitoriapc():
                    print("\nVocê perdeu! O PC fez Blackjack.")
                break

        if sum(bb.pontuacaodacarta) == 21:
            print("\nVocê venceu por Blackjack!")
        elif sum(bb.pontuacaodacarta) > 21:
            print(f"\nVocê ultrapassou 21 pontos. Vitória do PC.")

        print("Cartas da sua mão:", ", ".join(map(str, bb.cartasmao)))
        print("Sua pontuação final: ",sum(bb.pontuacaodacarta))
        print("\nCartas da mão do PC:", ", ".join(map(str, bb.cartaspc)))
        print("Pontuação final do PC: ",sum(bb.pontuacaopc))

    except ValueError:
        print("\n\nO valor digitado é inválido")

if __name__ == "__main__":
    main()