import bblackjack as bb


bb.inicializamao()
bb.inicializamaopc()
try:
    bb.mostramao()
    pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n\n"))
    while pergunta==1:
        bb.puxacarta()
        bb.mostramao()
        pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n\n"))
    if pergunta==2:
        bb.pcjoga()
        bb.mostramao()
        pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n\n"))
        while pergunta==1:
            bb.puxacarta()
            pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória\n\n"))
    if pergunta==3:
        if(bb.testavitoriapontos()):
            print("Parabéns. Você venceu!")
            print("Resultado:",sum(bb.pontuacaodacarta),"x",sum(bb.pontuacaopc))
        else:
            print("O PC venceu!")
except ValueError:
    print("\n\nO valor digitado é inválido")