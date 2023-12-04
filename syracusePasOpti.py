import time
depart = int(input("combien de boucles?  "))
maxGlobal = depart
itMax = 0
respSommet = 0
longueur = 0
respLongueur = 0
listechiffre= []
for i in range(1,depart):
    chiffre = i
    Sommet = i
    it=0
    itSommetLoc = 1
    #incomplete = False
    while chiffre !=1:
        #if chiffre in listechiffre:
            #incomplete=True
            #break
        if chiffre%2==0:
            chiffre = chiffre/2
        else:
            chiffre = (3*chiffre)+1
            if chiffre>=Sommet:
                Sommet=chiffre
                itSommetLoc = it
        
        #print(i, " | ", chiffre)
        #time.sleep(0.1)
        it = it+1
    ratio = i/Sommet
    #if incomplete==False:
    print("le depart ", i, " a ", it, " iterations, et un sommet ", Sommet, " soit un ratio de ", ratio, " \n")
    if Sommet>=maxGlobal:
        maxGlobal=Sommet
        itMax=itSommetLoc
        respSommet = i
        # print(i)
    if it>=longueur:
        longueur=it
        respLongueur = i
    #else:
        #print("le depart ", i, " a deja ete vu et donc skip \n")
print("=========================================================================================== \n")
print("La valeur la plus haute atteinte est de ", maxGlobal, "atteinte a la ", itMax,"eme iteration de la chaine de depart", respSommet, "\n")
print("La chaine la plus longue est de ", longueur, " atteinte par la chaine ", respLongueur)

