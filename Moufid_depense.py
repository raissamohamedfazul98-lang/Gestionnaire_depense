import pandas as pd
from pathlib import Path

FICHIER = Path("depenses.csv")

def afficher_depenses():
    if not FICHIER.exists():
        print("Aucune dépense enregistrée.")
        return
    df = pd.read_csv(FICHIER)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.sort_values(by="Date")
    print(df)

def calculer_balance():
    if not FICHIER.exists():
        print("Aucune dépense enregistrée.")
        return
    df = pd.read_csv(FICHIER)
    print("Balance totale :", df["Somme"].sum())

def supprimer_depense():
    if not FICHIER.exists():
        print("Aucune dépense enregistrée.")
        return
    df = pd.read_csv(FICHIER)
    print(df)
    index = int(input("Index de la dépense à supprimer : "))
    if index < 0 or index >= len(df):
        print("Index invalide.")
        return
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(FICHIER, index=False)
    print("Dépense supprimée.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Afficher les dépenses par date")
        print("2. Calculer la balance totale")
        print("3. Supprimer une dépense")
        print("4. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            afficher_depenses()
        elif choix == "2":
            calculer_balance()
        elif choix == "3":
            supprimer_depense()
        elif choix == "4":
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()