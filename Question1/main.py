import re

def somme_valeurs_etalonnage(fichier):

    somme = 0
    #ouverture du fichier et calcule de la somme
    with open(fichier, 'r') as file:
        for ligne in file:
            ligne = ligne.strip()
            #extraction des chiffres
            chiffres = re.findall('\\d', ligne)
            
            if len(chiffres) >= 2:
              
                valeur = int(chiffres[0] + chiffres[-1])
            elif len(chiffres) == 1:
                
                valeur = int(chiffres[0] * 2)
            else:
                
                continue
            
            somme += valeur

    return somme


nom_fichier = "Question1/document.txt"
somme_totale = somme_valeurs_etalonnage(nom_fichier)
print("La somme des valeurs d'étalonnage est : " + str(somme_totale))

