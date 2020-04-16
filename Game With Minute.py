A,B,C,D=map(int,input().split())
if A==C and B==D:
    dh,dm=24,0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
elif A<C and A+1==C:
    dh=0
    if B>D:
        dm=(60-B)+D
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    elif B<D:
        dm=D-B
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    else:
        dh=1
        dm=0
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
elif A>C:
    dh=(24-A)+C
    if B>D:
        dh=dh-1
        dm=(60-B)+D
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    elif B<D:
        dm=D-B
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    else:
        dm=0
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
elif A<C:
    dh=C-A
    if B>D:
        dh=dh-1
        dm=(60-B)+D
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    elif B<D:
        dm=D-B
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    else:
        dm=0
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
elif A==C:
    dh=0
    if B>D:
        dh=23
        dm=(60-B)+D
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    elif B<D:
        dm=D-B
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
    else:
        dm=0
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(dh), str(dm)))
