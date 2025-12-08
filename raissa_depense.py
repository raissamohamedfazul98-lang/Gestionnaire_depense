import csv
from datetime import datetime
from pathlib import Path
import argparse

FICHIER_CSV = Path("depenses.csv")

def ajouter_depense(montant, intitule, categorie):
    nouvel_entree = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "montant": montant,
        "intitule": intitule,
        "categorie": categorie
    }

    # Si le fichier n'existe pas → créer l'en-tête
    fichier_existe = FICHIER_CSV.exists()

    with FICHIER_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "montant", "intitule", "categorie"])
        if not fichier_existe:
            writer.writeheader()
        writer.writerow(nouvel_entree)

    print("Dépense ajoutée avec succès !")

def filtrer_depenses(categorie=None):
    if not FICHIER_CSV.exists():
        print("Aucune dépense enregistrée.")
        return

    with FICHIER_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            if categorie is None or ligne["categorie"] == categorie:
                print(ligne)

def main():
    parser = argparse.ArgumentParser(description="Gestionnaire de dépenses")
    parser.add_argument("--ajouter", action="store_true", help="Ajouter une dépense")
    parser.add_argument("--montant")
    parser.add_argument("--intitule")
    parser.add_argument("--categorie")
    parser.add_argument("--filtrer")

    args = parser.parse_args()

    if args.ajouter:
      if not args.montant or not args.intitule or not args.categorie:
        print("Erreur : montant, intitulé et catégorie sont obligatoires pour ajouter une dépense.")
        return
      
        ajouter_depense(args.montant, args.intitule, args.categorie)
    if args.filtrer:
        filtrer_depenses(args.filtrer)

if __name__ == "__main__":
    main()