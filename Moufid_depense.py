import pandas as pd
import argparse
from datetime import datetime
from pathlib import Path

FICHIER = Path("depenses.csv")

def initialiser_csv():
    if not FICHIER.exists():
        df = pd.DataFrame(columns=["Date", "Somme", "Intitulé", "Catégorie", "Balance"])
        df.to_csv(FICHIER, index=False)

def calculer_balance():
    if FICHIER.exists():
        df = pd.read_csv(FICHIER)
        return df["Somme"].sum()
    return 0

def ajouter_depense(somme, intitule, categorie):
    balance = calculer_balance() + somme
    nouvelle_ligne = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Somme": somme,
        "Intitulé": intitule,
        "Catégorie": categorie,
        "Balance": balance
    }
    df = pd.read_csv(FICHIER)
    df = pd.concat([df, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
    df.to_csv(FICHIER, index=False)
    print("✅ Dépense ajoutée avec succès !")

def filtrer_depenses(categorie):
    if not FICHIER.exists():
        print("Aucune dépense enregistrée.")
        return
    df = pd.read_csv(FICHIER)
    filtre = df[df["Catégorie"] == categorie]
    print(filtre)

def supprimer_depense(index):
    if not FICHIER.exists():
        print("Aucune dépense enregistrée.")
        return
    df = pd.read_csv(FICHIER)
    if index < 0 or index >= len(df):
        print("❌ Index invalide.")
        return
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(FICHIER, index=False)
    print(f"🗑️ Dépense à l’index {index} supprimée.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gestion des dépenses")
    parser.add_argument("--ajouter", nargs=3, metavar=("Somme", "Intitulé", "Catégorie"),
                        help="Ajouter une dépense")
    parser.add_argument("--balance", action="store_true", help="Afficher la balance totale")
    parser.add_argument("--filtrer", type=str, help="Filtrer les dépenses par catégorie")
    parser.add_argument("--supprimer", type=int, help="Supprimer une dépense par son index")

    args = parser.parse_args()
    initialiser_csv()

    if args.ajouter:
        somme = float(args.ajouter[0])
        intitule = args.ajouter[1]
        categorie = args.ajouter[2]
        ajouter_depense(somme, intitule, categorie)

    if args.balance:
        print("💰 Balance totale :", calculer_balance())

    if args.filtrer:
        filtrer_depenses(args.filtrer)

    if args.supprimer is not None:
        supprimer_depense(args.supprimer)