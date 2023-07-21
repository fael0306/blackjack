import bblackjack as bb


bb.inicializamao()
bb.inicializamaopc()
try:
    bb.mostramao()
    situacao = bb.testavitoriabj()
    while not situacao:
        pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n"))
        situacao = bb.testavitoriabj()
        if situacao:
            break
        if pergunta==1:
            bb.puxacarta()
            if(bb.testavitoriabj()):
                break
            bb.mostramao()
        if pergunta==2:
            bb.pcjoga()
            if bb.testavitoriapc():
                print("\nVocê perdeu! O PC fez Blackjack.")
                break
            else:
                print("\nO PC estourou com",sum(bb.pontuacaopc),"pontos.")
                print("\nVocê venceu!")
                break
        if pergunta==3:
            if bb.testavitoriabj():
                print("Você venceu por Blackjack.")
            elif bb.testavitoriapontos():
                print("\nParabéns. Você venceu!")
                print("\nResultado:",sum(bb.pontuacaodacarta),"x",sum(bb.pontuacaopc))
            elif bb.testavitoriapc():
                print("\nVocê perdeu! O PC fez Blackjack.")
            else:
                continue
            break
    if sum(bb.pontuacaodacarta)==21:
        print("\nVocê venceu por Blackjack!")
    elif sum(bb.pontuacaodacarta)>21:
        print("\nVocê ultrapassou 21 pontos. Vitória do PC com",sum(bb.pontuacaopc),"pontos.")
    
    print("Cartas da sua mão: ",", ".join(map(str, bb.cartasmao))) 
    print("Cartas da mão do PC: ",", ".join(map(str,bb.cartaspc)))
except ValueError:
    print("\n\nO valor digitado é inválido")