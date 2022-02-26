def affichage_regles():
    print('\n==============================================================')
    print('=== Rappel des règles  :')
    print('== - La pierre écrase les ciseaux et gagne.')
    print('== - La feuille enveloppe la pierre et gagne.')
    print('== - Les ciseaux découpent la feuille et gagnent.')
    print('== ')
    print('=== Le premier joueur qui gagne 3 manches gagne la partie')
    print('==============================================================\n')


def affichage_choix(nom_j1, choix_j1, nom_j2, choix_j2):
    print('\n==============================================================')
    print(f'== - Choix {nom_j1} : {choix_j1}')
    print(f'== - Choix {nom_j2} : {choix_j2}')
    print('==============================================================\n')


def saisie_joueur(nomJoueur):
    while True:
        saisie = input('> ' + nomJoueur + ' \n(1) - Pierre \n(2) - Feuille \n(3) - Ciseaux\nFaites votre choix : ')
        if saisie not in ["1", "2", "3"]:
            print("Proposition incorrecte, veuillez respecter le format souhaité")
        else:
            return int(saisie)
