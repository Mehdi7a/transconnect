import glob
import os
import pandas as pd
from tqdm import tqdm

# L'emplacement exact de votre dossier
DOSSIER_CIBLE = r"C:\Users\LENOVO\Desktop\Nouveau dossier"

# Recherche de tous les fichiers .parquet dans ce dossier
fichiers_parquet = glob.glob(os.path.join(DOSSIER_CIBLE, "*.parquet"))

if not fichiers_parquet:
    print(f"Aucun fichier .parquet trouvé dans le dossier : {DOSSIER_CIBLE}")
else:
    print(
        f"Trouvé {len(fichiers_parquet)} fichiers à convertir dans"
        f" '{DOSSIER_CIBLE}'.\n"
    )

    # Conversion de chaque fichier
    for chemin_parquet in fichiers_parquet:
        nom_fichier = os.path.basename(chemin_parquet)
        nom_sans_ext = os.path.splitext(nom_fichier)[0]

        # Le fichier CSV sera créé dans le même dossier
        chemin_csv = os.path.join(DOSSIER_CIBLE, f"{nom_sans_ext}.csv")

        print(f"Conversion de {nom_fichier}...")

        # Lecture du fichier Parquet
        df = pd.read_parquet(chemin_parquet)

        # Sauvegarde en CSV
        df.to_csv(chemin_csv, index=False)

    print("\nTerminé ! Tous les fichiers ont été convertis en CSV.")
