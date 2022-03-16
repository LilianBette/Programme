class Arbre (R):
    def __init__ (self,donnee,gauche,droite):
        """
        Classe Arbre.
            Cette classe effectue un arbre binaire avec des données.
                Argument [1] : R donnée de la racine (pour une feuille). ou
                Argument [3] : Donnée de la racine, arbre gauche , arbre droite.
                Vide() peut être utilisé pour un sous-arbre gauche ou droite vide.
        """
        self.donnee=0
        self.droite = ()
        self.gauche = ()

    def estVide (self):
        """
        Méthode estVide
            Cette méthode renvoi True ou False si l'arbre est vide ou non.
                Argument [0] : Aucun.
                Valeur de retour : Un boléen.
        """
        return False

    def racine(self):
        """
        Méthode racine
            Cette méthode renvoie la valeur de racine.
                Argument [0] : Aucun.
                Valeur de retour : valeur de la racine.
        """
        assert not self.estVide()
        return self.donnee
    

    def sousArbreGauche (self):
        """
        Méthode sousArbreGauche
            Cette méthode renvoie l'arbre à la gauche de la racine.
            Argument [0] : Aucun.
            Valeur de retour : Arbre.
        """
        assert not self.estVide()
        return self.gauhe

    def sousArbreDroit (self):
        """
        Méthode sousArbreDroit
            Cette méthode renvoie l'arbre à la droite de la racine.
            Argument [0] : Aucun.
            Valeur de retour : Arbre.
        """
        assert not self.estVide()
        return self.droite
