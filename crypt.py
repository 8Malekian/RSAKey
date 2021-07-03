import tools


def chiffrer(cle,pathtext):
    
    clepub=""
    try : 
        fichier = open (pathtext,"r")
        textadechiffrer = fichier.read()
        print ("text: " +textadechiffrer)
        fichier2 = open (cle,"r")
        clepub = fichier2.read()
        print ("clépub: "+clepub)
    except FileNotFoundError:
        print ("pas de clé ou pas de fichier")
    
    if tools.verifClepub (clepub):
        n,d=tools.extractCle(clepub,"pub")
        print("n:"+n)
        print("n:"+d)