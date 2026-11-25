
from datetime import datetime


class CompteBancaire:
    compteur = 0

    def __init__(self, solde_initial=0.0):
        CompteBancaire.compteur += 1
        self.identifiant = CompteBancaire.compteur
        self.__solde = solde_initial
        self.operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self.operations.append(
                f"{datetime.now()} - Dépôt : +{montant}€"
            )
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self.operations.append(
                f"{datetime.now()} - Retrait : -{montant}€"
            )
        else:
            print("Fonds insuffisants ou montant invalide.")

    def get_solde(self):
        return self.__solde

    def afficher_releve(self):
        print(f"Relevé du compte {self.identifiant} :")
        for operation in self.operations:
            print(operation)


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = [CompteBancaire()]

    @property
    def compte(self):
        return self.comptes[0]

    def ajouter_compte(self, solde_initial=0.0):
        nouveau_compte = CompteBancaire(solde_initial)
        self.comptes.append(nouveau_compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for compte in self.comptes:
            print(
                f"Compte N° {compte.identifiant}, "
                f"Solde : {compte.get_solde()}€"
            )


if __name__ == "__main__":

    # Création d'un client
    cli = Client("Yassir")

    # Opérations sur le premier compte
    cli.compte.deposer(300)
    cli.compte.retirer(50)

    # Ajout d'un deuxième compte
    cli.ajouter_compte(1000)
    cli.comptes[1].deposer(200)

    # Affichage des comptes
    cli.afficher()

    # Relevé des opérations
    print("\nHistorique des opérations :")
    cli.compte.afficher_releve()
