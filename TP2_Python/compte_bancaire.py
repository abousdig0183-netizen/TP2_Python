
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : +{montant} €")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : -{montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    def afficher_historique(self):
        print("Historique des opérations :")
        for operation in self._operations:
            print(operation)

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux_interet=0.03):
        super().__init__(titulaire, solde_initial)
        self.taux_interet = taux_interet

    def calculer_interet(self):
        interet = self.solde * self.taux_interet
        return interet


if __name__ == "__main__":

    # Test CompteBancaire
    compte = CompteBancaire("Ali", 1000)

    compte.deposer(200)
    compte.retirer(150)

    print(compte)
    print("Solde accessible (lecture) :", compte.solde)
    compte.afficher_historique()

    print("\n-------------------------")

    # Test CompteEpargne
    epargne = CompteEpargne("Sara", 5000, 0.04)

    print(epargne)
    print("Taux d'intérêt :", epargne.taux_interet * 100, "%")
    print("Intérêt annuel :", epargne.calculer_interet(), "€")
