import bblackjack as bb


bb.inicializamao()
bb.inicializamaopc()
try:
    bb.mostramao()
    while bb.testavitoriabj()==False:
        pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n\n"))
        if bb.testavitoriabj==True:
            break
        if pergunta==1:
            bb.puxacarta()
            bb.mostramao()
        if pergunta==2:
            bb.pcjoga()
            if bb.testavitoriapc():
                print("Você perdeu! O PC fez Blackjack.")
                break
            else:
                print("O PC estourou com",sum(bb.pontuacaopc),"pontos.")
                print("Você venceu!")
                break
        if pergunta==3:
            if bb.testavitoriapontos():
                print("Parabéns. Você venceu!")
                print("Resultado:",sum(bb.pontuacaodacarta),"x",sum(bb.pontuacaopc))
                break
            else:
                print("O PC venceu com",sum(bb.pontuacaopc),"pontos!")
                break
    if sum(bb.pontuacaodacarta)==21:
        print("Você venceu por Blackjack!")
    elif sum(bb.pontuacaodacarta)>21:
        print("Você ultrapassou 21 pontos. Vitória do PC com",sum(bb.pontuacaopc),"pontos.")
except ValueError:
    print("\n\nO valor digitado é inválido")