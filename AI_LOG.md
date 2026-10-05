## Entrée 05/10/2026
- Outil IA utilisé : Claude
- Prompt : "Voici le cahier des charges de mon projet Django TransConnect (diagramme de classe + contraintes de modélisation). Écris-moi le modèle Offre dans OffresApp/models.py avec les champs prix, delai_jours, statut, date_proposition et les clés étrangères vers Expedition, Entreprise (transporteur) et Vehicule."
- Sortie obtenue (résumé) : modèle Offre avec prix en CharField, date_proposition en auto_now, delai_jours en IntegerField et un save() inutile.
- Écarts identifiés vs cahier des charges :
  1. prix en CharField au lieu de DecimalField
  2. delai_jours en IntegerField au lieu de PositiveIntegerField
  3. date_proposition en auto_now au lieu de auto_now_add
  4. save() redondant : il appelle seulement super().save() sans rien ajouter
- Correction apportée et justification :
  1. DecimalField(max_digits=10, decimal_places=2) : un prix est un nombre, on doit pouvoir le trier et faire des calculs
  2. PositiveIntegerField : un délai en jours ne peut pas être négatif
  3. auto_now_add=True : la date ne doit être fixée qu'à la création de l'offre, pas modifiée à chaque save()
  4. save() supprimé (ou remplacé par la logique d'acceptation) car il n'apportait rien