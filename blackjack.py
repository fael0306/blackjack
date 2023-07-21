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
            bb.mostramao()
        if pergunta==3:
            if bb.testavitoriapontos():
                print("Parabéns. Você venceu!")
                print("Resultado:",sum(bb.pontuacaodacarta),"x",sum(bb.pontuacaopc))
            else:
                print("O PC venceu!")
except ValueError:
    print("\n\nO valor digitado é inválido")