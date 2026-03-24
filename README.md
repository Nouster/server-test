# Gestion de Produits API

Application de gestion de produits avec Backend FastAPI et Frontend moderne (Tailwind CSS).

## Fonctionnalités

- CRUD complet (Créer, Lire, Mettre à jour, Supprimer)
- Données initiales chargées via JSON
- Interface Dashboard moderne et responsive
- Suite de tests unitaires avec 100% de couverture
- Conteneurisation avec Docker

## Installation Locale

1. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

2. Lancez le serveur :

   ```bash
   uvicorn backend.main:app --reload
   ```

3. Accédez à l'application :
   - Frontend : `http://localhost:8000`
   - Documentation API : `http://localhost:8000/docs`

## Docker

1. Construisez l'image :

   ```bash
   docker build -t product-app .
   ```

2. Lancez le conteneur :

   ```bash
   docker run -p 8000:8000 product-app
   ```

## Tests et Qualité

- Exécutez les tests :

  ```bash
  pytest
  ```

- Vérifiez la couverture :

  ```bash
  pytest --cov=backend backend/tests/
  ```

- Analyse de complexité (Radon) :

  ```bash
  radon cc backend -a
  ```
