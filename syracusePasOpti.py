import time
def syracuseUntil(choix):
    if choix==1:
        depart = int(input("quel depart specifique? "))
    else:
        depart = int(input("combien de boucles?  "))
    maxGlobal = depart
    itMax = 0
    respSommet = 0
    longueur = 0
    respLongueur = 0
    listechiffre= []
    for i in range(1,depart):
        chiffre = i
        valeur = i
        Sommet = i
        if choix==1:
            chiffre = depart
            casseToi = True
            valeur = depart
            Sommet=valeur
        it=0
        itSommetLoc = 1
        #incomplete = False
        while chiffre !=1:
            #if chiffre in listechiffre:
                #incomplete=True
                #break
            caMonte=False
            if chiffre%2==0:
                chiffre = chiffre/2
                caMonte=False
            else:
                chiffre = (3*chiffre)+1
                caMonte=True
                if chiffre>=Sommet:
                    Sommet=chiffre
                    itSommetLoc = it
            if casseToi==True:
                if caMonte==False:
                    strMonte = "on est descendus"
                else:
                    strMonte = "on est montes   "
                print(it, " | "+strMonte+" | ", chiffre)
            #time.sleep(0.1)
            it = it+1
        ratio = valeur/Sommet
        #if incomplete==False:
        print("le depart ", valeur, " a ", it, " iterations, et un sommet ", Sommet, " soit un ratio de ", ratio, " \n")
        if Sommet>=maxGlobal:
            maxGlobal=Sommet
            itMax=itSommetLoc
            respSommet = valeur
            # print(i)
        if it>=longueur:
            longueur=it
            respLongueur = valeur
        if casseToi==True:
            break
        #else:
            #print("le depart ", i, " a deja ete vu et donc skip \n")
    print("=========================================================================================== \n")
    print("La valeur la plus haute atteinte est de ", maxGlobal, "atteinte a la ", itMax,"eme iteration de la chaine de depart", respSommet, "\n")
    print("La chaine la plus longue est de ", longueur, " atteinte par la chaine ", respLongueur)

choisis = int(input("voulez vous un certain depart (1) ou une liste jusqu'a (2)?  "))
syracuseUntil(choisis)






