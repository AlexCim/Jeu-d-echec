joueur=1
largeur=9
hauteur=9
colonneRoiNoir=5
ligneRoiNoir=7
colonneRoiBlanc=5
ligneRoiBlanc=0
grille=[[0]*largeur for i in range(hauteur)]
listePieces=["_","♜","♞","♝","♚","♛","♟","♘","♙","♔","♕","♗","♖","A","B","C","D","E","F","G","H"]    #liste des pièces

for i in range(21):
    listePieces[i]=i

def grilleEchec():
    """Va afficher la grille d'échec vide avec la liste des pièces du jeu"""
    listePieces=["_","♜","♞","♝","♚","♛","♟","♘","♙","♔","♕","♗","♖","A","B","C","D","E","F","G","H"]
    for j in range(hauteur-1,-1,-1):
        print("|",end="")
        for i in range(largeur):
            print(listePieces[grille[i][j]],end="|")
        print("")
    for i in range(largeur):
        print("|{}".format(i),end="")        #Numérote les colonnes de 0 à 8
    print("|")
    print("\n")



def GrilleInit():
    """Cette fonction va créer la grille avec les pièces intialement placer."""
    grille[1][0]=listePieces[12]
    grille[8][0]=listePieces[12]
    for i in range(8):
        grille[i+1][1]=listePieces[8]
    for i in range(8):
        grille[i+1][6]=listePieces[6]
    grille[2][0]=listePieces[7]
    grille[7][0]=listePieces[7]
    grille[3][0]=listePieces[11]
    grille[6][0]=listePieces[11]
    grille[4][0]=listePieces[10]
    grille[5][0]=listePieces[9]
    grille[1][7]=listePieces[1]
    grille[8][7]=listePieces[1]
    grille[2][7]=listePieces[2]
    grille[7][7]=listePieces[2]
    grille[3][7]=listePieces[3]
    grille[6][7]=listePieces[3]
    grille[4][7]=listePieces[5]
    grille[5][7]=listePieces[4]
    for i in range(8):
        grille[0][i]=listePieces[13+i]         #Nomme les différentes lignes de l'échiquier
        
GrilleInit()
def Deplacement():
    """Cette fonction permet le déplacements des pièces"""
    global joueur
    global colonneRoiNoir
    global ligneRoiNoir
    global colonneRoiBlanc
    global ligneRoiBlanc
    grilleEchec()
    
    if joueur%2==0:
        tourDuRoiNoir=0
        print("Le tour du joueur 2.")
        print("♟","♝","♜","♞","♛","♚")
        pieceNoir=int(input("Quelle pièce entre 1 et 6 voulez-vous jouer?"))
        coordonnées=input("Quel est votre déplacement. Exemple: 2A-3C \n").split('-')    #recupere les coordonnées sous la forme 2A-3C por faciliter les joueurs
        colonneInit=int(coordonnées[0][0])
        ligneInit=coordonnées[0][1]
        colonneArriv=int(coordonnées[1][0])
        ligneArriv=coordonnées[1][1]
        code=ord(ligneInit)
    
        code2=ord(ligneArriv)
        ligneI=code-65
        ligneA=code2-65
        verif=0
        if colonneInit<1 or colonneInit>8 or colonneArriv<1 or colonneArriv>8 or code<65 or code>72 or code2<65 or code2>72:
             grilleEchec()
             print("Vous êtes hors grille. Vous devez choisir entre 1,2,3,4,5,6,7,8 pour les colonnes et A,B,C,D,E,F,G,H pour les lignes")             #permet aux joueurs de rester dans la grille
        
        
        elif grille[colonneInit][ligneI]==listePieces[0]:
             grilleEchec()
             ("Vous voulez déplacé une case vide?")      #vérifie si il ya bien une pièce aux coordonnées initiales
        
        
        elif grille[colonneArriv][ligneA]==listePieces[1] or grille[colonneArriv][ligneA]==listePieces[2] or grille[colonneArriv][ligneA]==listePieces[3] or grille[colonneArriv][ligneA]==listePieces[4] or grille[colonneArriv][ligneA]==listePieces[5] or grille[colonneArriv][ligneA]==listePieces[6]:
             grilleEchec()
             print("On mange pas ses propres pièces!!")                  #empêche de manger ses propres pièces
        
        
        elif pieceNoir==3:
            if colonneInit!=colonneArriv and ligneInit!=ligneArriv:         #condition de déplacement de la tour noir
                 grilleEchec()
                 print("Mauvais déplacement de la Tour") 
            elif colonneInit==colonneArriv and ligneI<ligneA:
                for i in range(ligneI+1,ligneA):
                    a=grille[colonneInit][i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif colonneInit==colonneArriv and ligneI>ligneA:
                for i in range(1,abs(ligneA-ligneI)):
                    a=grille[colonneInit][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit<colonneArriv:
                for i in range(colonneInit+1,colonneArriv):
                    b=grille[i][ligneA]==listePieces[0]
                    if b==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit>colonneArriv:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            else:
                 grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                 grille[colonneInit][ligneI]=listePieces[0]
                 grilleEchec()
                 joueur+=1
        
        elif pieceNoir==4 and ((abs(colonneInit-colonneArriv)!=2 or abs((ligneA)-(ligneI))!=1) and (abs(colonneInit-colonneArriv)!=1 or abs((ligneA)-(ligneI))!=2)):
             grilleEchec()                                                  #condition de déplacement du cavalier noir
             print("Mauvais déplacement du cavalier")
        
        elif pieceNoir==2:
            if abs(colonneInit-colonneArriv)!=abs((ligneA)-(ligneI)):   #condition de déplacement du fou noir
                grilleEchec()
                print("Mauvais déplacement du fou")
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            else:
                grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                grille[colonneInit][ligneI]=listePieces[0]
                grilleEchec()
                joueur+=1
             
             
        elif pieceNoir==1:
            if ligneInit=='G' and colonneInit==colonneArriv and (ligneI)==(ligneA)+2 and grille[colonneArriv][ligneA]==listePieces[0] and grille[colonneArriv][(ligneA)+1]==listePieces[0]:
                if ligneArriv=='A':
                    nouvellePiece=int(input("Quelle pièce voulez-vous placer? ♜ ♞ ♝ ♚ ♕ ♟"))
                    grille[colonneArriv][ligneA]=listePieces[nouvellePiece]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
            
            elif (abs(colonneInit-colonneArriv)==1 and (ligneI)==(ligneA)+1) and grille[colonneArriv][ligneA]!=listePieces[0]:
                if ligneArriv=='A':
                    nouvellePiece=int(input("Quelle pièce voulez-vous placer? ♜ ♞ ♝ ♚ ♕ ♟"))
                    grille[colonneArriv][ligneA]=listePieces[nouvellePiece]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                
            elif (colonneInit!=colonneArriv or (ligneI)!=(ligneA)+1):
                grilleEchec()
                print("Mauvais déplacement du pion")
            
            elif (colonneInit==colonneArriv and (ligneI)==(ligneA)+1) and grille[colonneArriv][ligneA]!=listePieces[0]:
                grilleEchec()
                print("Mauvais déplacement du pion")
            else:
                if ligneArriv=='A':
                    nouvellePiece=int(input("Quelle pièce voulez-vous placer? ♜ ♞ ♝ ♚ ♕ ♟"))
                    grille[colonneArriv][ligneA]=listePieces[nouvellePiece]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                
                
        elif pieceNoir==6:                                #condition de déplacement du roi noir
             if (abs(colonneInit-colonneArriv)!=1 and abs(colonneInit-colonneArriv)!=0) or (abs((ligneI)-(ligneA))!=1 and abs((ligneI)-(ligneA))!=0):
                  grilleEchec()
                  print("Mauvais déplacement du roi.")
             elif colonneInit==colonneArriv-2 and ligneInit==H and ligneArriv==H and grille[8][0]==listePieces[1] and tourDuRoiNoir==0:                          #le petit roque
                  tourDuRoiNoir+=1
                  grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                  grille[colonneInit][ligneI]=listePieces[0]
                  grille[8][0]=grille[6][0]
                  grille[8][0]=listesPieces[0]
                  grilleEchec()
                  joueur+=1
                  colonneRoiNoir=colonneArriv
                  ligneRoiNoir=ligneA
             elif colonneInit==colonneArriv+2 and ligneInit==H and ligneArriv==H and grille[1][0]==listePieces[1] and tourDuRoiNoir==0:                              #le grand roque
                  tourDuRoiNoir+=1
                  grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                  grille[colonneInit][code-65]=listePieces[0]
                  grille[1][0]=grille[4][0]
                  grille[1][0]=listesPieces[0]
                  grilleEchec()
                  joueur+=1
                  colonneRoiNoir=colonneArriv
                  ligneRoiNoir=ligneA
             else:
                  grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                  grille[colonneInit][ligneI]=listePieces[0]
                  grilleEchec()
                  joueur+=1
                  tourDuRoiNoir+=1
                  colonneRoiNoir=colonneArriv
                  ligneRoiNoir=code2-65
                  
        elif pieceNoir==5:                              #condition de déplacement de la reine 
            if abs(colonneInit-colonneArriv)!=abs((ligneI)-(ligneA)) and (colonneInit!=colonneArriv and ligneI!=ligneA):
                grilleEchec()
                print("Mauvais déplacement de la reine")
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif colonneInit==colonneArriv and ligneI<ligneA:
                for i in range(ligneI+1,ligneA):
                    a=grille[colonneInit][i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif colonneInit==colonneArriv and ligneI>ligneA:
                for i in range(1,abs(ligneA-ligneI)):
                    a=grille[colonneInit][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit<colonneArriv:
                for i in range(colonneInit+1,colonneArriv):
                    b=grille[i][ligneA]==listePieces[0]
                    if b==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit>colonneArriv:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            else:
                grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                grille[colonneInit][ligneI]=listePieces[0]
                grilleEchec()
                joueur+=1
                

        else:                              #suite au changement du programme cela devient inutile. Mais risqué de supprimer
             grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
             grille[colonneInit][ligneI]=listePieces[0]
             grilleEchec()
             joueur+=1
        
             
             
             #la deuxieme partie est la même que pour les pièces noirs mais pour les pièces blanches.
             
             
    else:
        tourDuRoiBlanc=0
        print("Le tour du joueur 1.")
        print("♙","♗","♖","♘","♕","♔")
        pieceBlanche=int(input("Quelle pièce entre 1 et 6 voulez-vous jouer?"))
        coordonnées=input("Quel est votre déplacement. Exemple: 2A-3C \n").split('-')
        colonneInit=int(coordonnées[0][0])
        ligneInit=coordonnées[0][1]
        colonneArriv=int(coordonnées[1][0])
        ligneArriv=coordonnées[1][1]
        code=ord(ligneInit)
        code2=ord(ligneArriv)
        ligneI=code-65
        ligneA=code2-65
        verif=0
        if colonneInit<1 or colonneInit>8 or colonneArriv<1 or colonneArriv>8 or code<65 or code>72 or code2<65 or code2>72:
             grilleEchec()
             print("Vous êtes hors grille. Vous devez choisir entre 1,2,3,4,5,6,7,8 pour les colonnes et A,B,C,D,E,F,G,H pour les lignes")
        
        elif grille[colonneInit][ligneI]==listePieces[0]:
             grilleEchec()
             ("Vous voulez déplacé une case vide?")
        
        
        elif grille[colonneArriv][ligneA]==listePieces[7] or grille[colonneArriv][ligneA]==listePieces[8] or grille[colonneArriv][ligneA]==listePieces[9] or grille[colonneArriv][ligneA]==listePieces[10] or grille[colonneArriv][ligneA]==listePieces[11] or grille[colonneArriv][ligneA]==listePieces[12]:
             grilleEchec()
             print("On mange pas ses propres pièces!!")
        
        
        elif pieceBlanche==3:
            if colonneInit!=colonneArriv and ligneInit!=ligneArriv:         #condition de déplacement de la tour noir
                 grilleEchec()
                 print("Mauvais déplacement de la Tour") 
            elif colonneInit==colonneArriv and ligneI<ligneA:
                for i in range(ligneI+1,ligneA):
                    a=grille[colonneInit][i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif colonneInit==colonneArriv and ligneI>ligneA:
                for i in range(1,abs(ligneA-ligneI)):
                    a=grille[colonneInit][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit<colonneArriv:
                for i in range(colonneInit+1,colonneArriv):
                    b=grille[i][ligneA]==listePieces[0]
                    if b==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit>colonneArriv:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la Tour")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
                
            else:
                 grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                 grille[colonneInit][ligneI]=listePieces[0]
                 grilleEchec()
                 joueur+=1
        
        elif pieceBlanche==4 and ((abs(colonneInit-colonneArriv)!=2 or abs((ligneA)-(ligneI))!=1) and (abs(colonneInit-colonneArriv)!=1 or abs((ligneA)-(ligneI))!=2)):
             grilleEchec()
             print("Mauvais déplacement du cavalier")
             
        elif pieceBlanche==2:
            if abs(colonneInit-colonneArriv)!=abs((ligneA)-(ligneI)):
                grilleEchec()
                print("Mauvais déplacement du fou")
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement du fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            else:
                grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                grille[colonneInit][ligneI]=listePieces[0]
                grilleEchec()
                joueur+=1
        
        elif pieceBlanche==1:
            if ligneInit=='B' and colonneInit==colonneArriv and (ligneI)==(ligneA)-2 and grille[colonneArriv][ligneA]==listePieces[0] and grille[colonneArriv][(ligneA)-1]==listePieces[0]:
                if ligneArriv=='H':
                    nouvellePiece=int(input("Quelle pièce voulez-vous placer? ♘ ♙ ♗ ♔ ♛ ♖"))
                    grille[colonneArriv][ligneA]=listePieces[6+nouvellePiece]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
            
            elif (abs(colonneInit-colonneArriv)==1 and (ligneI)==(ligneA)-1) and grille[colonneArriv][ligneA]!=listePieces[0]:
                if ligneArriv=='H':
                    nouvellePiece=int(input("Quelle pièce voulez-vous placer? ♘ ♙ ♗ ♔ ♛ ♖"))
                    grille[colonneArriv][ligneA]=listePieces[6+nouvellePiece]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                
            elif (colonneInit!=colonneArriv or (ligneI)!=(ligneA)-1):
                grilleEchec()
                print("Mauvais déplacement du pion")
            
            elif (colonneInit==colonneArriv and (ligneI)==(ligneA)-1) and grille[colonneArriv][ligneA]!=listePieces[0]:
                grilleEchec()
                print("Mauvais déplacement du pion")
            
            else:
                if ligneArriv=='H':
                    nouvellePiece=int(input("Quelle pièce voulez-vous placer? ♘ ♙ ♗ ♔ ♛ ♖"))
                    grille[colonneArriv][ligneA]=listePieces[6+nouvellePiece]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]      #condition de déplacement du pion noir avec prise sur la diagonale si il ya une pièce
                
                    grille[colonneInit][ligneI]=listePieces[0]   #on déplace la pièce puis on remplace l'emplacement initial par _
                    grilleEchec()
                    joueur+=1
        elif pieceBlanche==6:
             if (abs(colonneInit-colonneArriv)!=1 and abs(colonneInit-colonneArriv)!=0) or (abs((ligneI)-(ligneA))!=1 and abs((ligneI)-(ligneA))!=0):
                  grilleEchec()
                  print("Mauvais déplacement du roi.")
             elif colonneInit==colonneArriv-2 and ligneInit==A and ligneArriv==A and grille[8][7]==listePieces[1] and tourDuRoiBlanc==0:                          #le petit roque
                  tourDuRoiBlanc+=1
                  grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                  grille[colonneInit][ligneI]=listePieces[0]
                  grille[8][7]=grille[6][7]
                  grille[8][7]=listesPieces[0]
                  grilleEchec()
                  joueur+=1
                  colonneRoiBlanc=colonneArriv
                  ligneRoiBlanc=ligneA
             elif colonneInit==colonneArriv+2 and ligneInit==A and ligneArriv==A and grille[1][7]==listePieces[1] and tourDuRoiBlanc==0:                              #le grand roque
                  tourDuRoiBlanc+=1
                  grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                  grille[colonneInit][ligneI]=listePieces[0]
                  grille[1][7]=grille[4][7]
                  grille[1][7]=listesPieces[0]
                  grilleEchec()
                  joueur+=1
                  colonneRoiBlanc=colonneArriv
                  ligneRoiBlanc=ligneA
                 
             else:
                  grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                  grille[colonneInit][ligneI]=listePieces[0]
                  grilleEchec()
                  joueur+=1
                  tourDuRoi+=1
                  colonneRoiBlanc=colonneArriv
                  ligneRoiBlanc=ligneA
                  
        elif pieceBlanche==5:
            if abs(colonneInit-colonneArriv)!=abs((ligneI)-(ligneA)) and (colonneInit!=colonneArriv and ligneI!=ligneA):
                grilleEchec()
                print("Mauvais déplacement de la reine")
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit<colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit+i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI<ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI+i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine fou")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif abs(colonneInit-colonneArriv)==abs(ligneA-ligneI) and colonneInit>colonneArriv and ligneI>ligneA:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif colonneInit==colonneArriv and ligneI<ligneA:
                for i in range(ligneI+1,ligneA):
                    a=grille[colonneInit][i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif colonneInit==colonneArriv and ligneI>ligneA:
                for i in range(1,abs(ligneA-ligneI)):
                    a=grille[colonneInit][ligneI-i]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit<colonneArriv:
                for i in range(colonneInit+1,colonneArriv):
                    b=grille[i][ligneA]==listePieces[0]
                    if b==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            elif ligneInit==ligneArriv and colonneInit>colonneArriv:
                for i in range(1,abs(colonneArriv-colonneInit)):
                    a=grille[colonneInit-i][ligneI]==listePieces[0]
                    if a==False:
                        verif+=1
                if verif!=0:
                    grilleEchec()
                    print("Mauvais déplacement de la reine")
                else:
                    grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                    grille[colonneInit][ligneI]=listePieces[0]
                    grilleEchec()
                    joueur+=1
            else:
                grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
                grille[colonneInit][ligneI]=listePieces[0]
                grilleEchec()
                joueur+=1
            
        else:
             grille[colonneArriv][ligneA]=grille[colonneInit][ligneI]     #on déplace la pièce puis on remplace l'emplacement initial par _
             grille[colonneInit][ligneI]=listePieces[0]
             grilleEchec()
             joueur+=1
    
    
    
     


    
A=0                                                        #ces lignes vont permettre de verifier si il ya présence des rois. Si oui le jeu continue si non on donne le gagnant.
while A!=1:
    Deplacement()
    if grille[colonneRoiNoir][ligneRoiNoir]!=listePieces[4]:
        A+=1
        print("Le joueur n°1 a gagné!!!")
    elif grille[colonneRoiBlanc][ligneRoiBlanc]!=listePieces[9]:
        A+=1
        print("Le joueur n°2 a gagné!!!")