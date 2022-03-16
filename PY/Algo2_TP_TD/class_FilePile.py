

class FilePile:
    contenu = []
    def __init__(self, contenu = None):
        if contenu is None:
            contenu = []
        self.contenu = contenu

    def copier(self, autrePile):
        self.contenu = autrePile.contenu

    def accesTete(self):
        if len(self.contenu) == 0:
            return None
        return self.contenu[0]

    def accesSommet(self):
        if len(self.contenu) == 0:
            return None
        return self.contenu[-1]

    def defiler(self):
        if len(self.contenu) == 0:
            return None
        x = self.contenu[0] 
        self.contenu = self.contenu[1:]
        return x

    def depiler(self):
        if len(self.contenu) == 0:
            return None
        x = self.contenu[-1] 
        self.contenu = self.contenu[:-1]
        return x

    def rempiler(self, element):
        self.contenu.append(element)

    def __len__(self):
        return len(self.contenu)

    def __repr__(self):
        return "cette pile contient : " + ",".join([str(e) for e in self.contenu])


## 1) ##

pole = FilePile([1, 2, 3])
print(pole.depiler())
print(pole)

def inverser(pile):
    nouvelle_pile = FilePile()
    while len(pile) > 0:
        nouvelle_pile.rempiler(pile.depiler())
    return nouvelle_pile

pile = FilePile([1, 2, 3])
print("\nDEBUT : ",pile)
print("\nSI inversion,", inverser(pile))
## fin 1) ##

## 2) ##
def recopie(pile):
    nouvelle_pile = FilePile()
    nouvelle_pile.copier(pile)
    while len(pile) > 0:
        nouvelle_pile.rempiler(pile.defiler())
    return nouvelle_pile

pile_2 = FilePile([1, 2, 3])
print("\nSI copie: ", recopie(pile_2))
## fin 2) ##

## 3) ##
def doubler(pile):
    nouvelle_pile = FilePile()
    while len(pile) > 0 :
        nouvelle_pile.rempiler(pile.defiler())
        nouvelle_pile.rempiler(nouvelle_pile.accesSommet())
    return nouvelle_pile

pile_3 = FilePile([1, 2, 3])
print("\nSI doublement des éléments: ", doubler(pile_3))
## fin 3) ##

## 4) ##
def multiplier_pile(pile):
    nb_element = len(pile)
    for i in range(nb_element):
        pile.rempiler(2 * pile.defiler())
    return pile

pile_4 = FilePile([1, 2, 3])
print("\nSI *2 aux éléments: ", multiplier_pile(pile_4))
## fin 4) ##

## 5) ##

def expr_polonaise(pile):
    pile = inverser(pile)
    while len(pile) > 1:
        num1 = pile.depiler()
        num2 = pile.depiler()
        ope = pile.depiler()
        resultat = 0
        if ope == "+":
            resultat = num1 + num2
        elif ope == "*":
            resultat = num1 * num2
        pile.rempiler(resultat)
    return pile.depiler()

pile_5 = FilePile([2, 3, "+", 2, "*"])
print("\nrésultat de 2 3 + 4* = ", expr_polonaise(pile_5))

## fin 5) ##
