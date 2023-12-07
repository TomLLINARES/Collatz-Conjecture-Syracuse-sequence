import matplotlib.pyplot as plt
import time
import argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("queryType")
parser.add_argument("number")
#parser.add_argument("GraphType")
args= parser.parse_args()

def syracuseUntil(choix):
    #if choix==1:
    #    depart = int(input("quel depart specifique? "))
    #else:
    #    depart = int(input("combien de boucles?  "))
    depart=int(args.number)
    maxGlobal = depart
    itMax = 0
    respSommet = 0
    longueur = 0
    respLongueur = 0
    valeursConnues = set()
    casseToi=False
    x = []
    y = []
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
        incomplete = False
        while chiffre !=1:
            if choix==1:
                y.append(chiffre)
                x.append(it)
            if chiffre in valeursConnues:
                incomplete=True
                break
            valeursConnues.add(chiffre)
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
        #if incomplete==True:
            #print("valeur skip chiale :):):):):):) ")
        #else:
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
    maxGlobal=int(maxGlobal)

    #strMaximum = str(maxGlobal)
    #listMax = []
    #strfin =''
    #for u in range((len(strMaximum)//3)+1):
    #    listMax.append(strMaximum[3*u]+strMaximum[3*u+1]+strMaximum[3*u+2])
    #    strfin=strfin+listMax[u]+' '
    #print('       ', strfin)
    if choix==1:
        #if GraphType =='scatter':
            #DataGraph=(x, y, color='red', marker='o', s=100, label='Data Points')
        
            #plt.scatter(x, y, color='red', markers='o', s=100, label='Data Points')
        #else: #GraphType == 'plot':
        plt.plot(x,y,linewidth=2.0)

        plt.xlabel('Iterations')
        plt.ylabel('Altitude')
        strTitre = 'Chaine '+str(depart)
        plt.title(strTitre)

        #plt.legend()

        plt.show()
    print("La valeur la plus haute atteinte est de ", maxGlobal, "atteinte a la ", max(it, itMax),"eme iteration de la chaine de depart", respSommet, "\n")
    print("La chaine la plus longue est de ", longueur, " atteinte par la chaine ", respLongueur)

#choisis = int(input("voulez vous un certain depart (1) ou une liste jusqu'a (2)?  "))
syracuseUntil(int(args.queryType))






