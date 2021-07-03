import base64
import random
import tools

def decrypt(cle,pathtext):
    clepriv=""
    try : 
        fichier = open (pathtext,"r")
        textadechiffrer = fichier.read()
        print (textadechiffrer)
        fichier2 = open (cle,"r")
        cleprive = fichier2.read()
        print (clepriv)
    except FileNotFoundError:
        print ("pas de clé ou pas de fichier")
    
    if tools.verifClepriv (clepriv):
        n,d=tools.extractCle(clepriv,privee)
        print("n:"+n)
        print("n:"+d)
        






     