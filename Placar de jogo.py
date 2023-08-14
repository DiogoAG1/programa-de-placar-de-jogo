time1 = int(input("Digite o numero de gols do primeiro time:"))
time2 = int(input("Digite o numero de gols do segundo time:"))

if time1 == time2:
    print ('O jogo terminou empatado')
elif time1 > time2:
        print (f"O primeiro time venceu com {time1} gols")
else:
            print (f"O segundo time ganhou com {time2} gols")