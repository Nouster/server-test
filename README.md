# Gestion de Produits - Boutique en Ligne (Projet DevOps)

Ce projet est une application complète de gestion de produits (CRUD) conçue pour répondre aux exigences d'un pipeline d'intégration et de déploiement continu (CI/CD) moderne.

## 📋 Contexte du Projet

Développement d'un backend en Python (FastAPI) pour une boutique en ligne, incluant une interface frontend moderne, une suite de tests automatisés, et une infrastructure DevOps (Jenkins & SonarQube).

## 🚀 Fonctionnalités

- **Backend CRUD** : Gestion des produits (id, nom, description, prix, quantité).
- **Frontend Dashboard** : Interface interactive avec Tailwind CSS.
- **Données Initiales** : Chargement automatique via `backend/products.json`.
- **Infrastructure** : Dockerisation complète et orchestration via Docker Compose.
- **CI/CD** : Pipeline Jenkins automatisé avec analyse de qualité SonarQube.

## 📁 Structure du Projet

- `backend/` : Code source de l'API FastAPI et modèles.
- `frontend/` : Interface utilisateur (HTML/JS/Tailwind).
- `backend/tests/` : Suite de tests unitaires (Pytest).
- `Dockerfile` : Configuration de l'image de production.
- `docker-compose.yml` : Orchestration Jenkins, SonarQube et Postgres.
- `Jenkinsfile` : Script de pipeline CI/CD.

## 🛠️ Installation et Utilisation

### 1. Installation Locale (Développement)

```bash
# Installation des dépendances
pip install -r requirements.txt

# Lancement du serveur (API + Frontend)
uvicorn backend.main:app --reload
```

Accès : `http://localhost:8000`

### 2. Utilisation avec Docker

```bash
# Construction et lancement de l'application
docker build -t product-app .
docker run -p 8000:8000 product-app
```

### 3. Environnement DevOps (Jenkins & SonarQube)

```bash
# Lancement de toute l'infrastructure
docker-compose up -d
```

- **Jenkins** : `http://localhost:8081`
- **SonarQube** : `http://localhost:9000`

## 🧪 Qualité du Code et Tests

### Tests Unitaires (Couverture > 80%)

```bash
# Exécuter les tests avec rapport de couverture
pytest --cov=backend backend/tests/
```

### Analyse de Complexité (Radon)

```bash
# Vérifier la complexité cyclomatique
radon cc backend -a
```

## 📖 Documentation de l'API CRUD

| Méthode    | Endpoint         | Description                       |
| :--------- | :--------------- | :-------------------------------- |
| **GET**    | `/products`      | Liste tous les produits           |
| **GET**    | `/products/{id}` | Détails d'un produit spécifique   |
| **POST**   | `/products`      | Créer un nouveau produit          |
| **PUT**    | `/products/{id}` | Mettre à jour un produit existant |
| **DELETE** | `/products/{id}` | Supprimer un produit              |

## ⚙️ Pipeline CI/CD (Jenkins)

Le pipeline automatisé (`Jenkinsfile`) exécute les étapes suivantes :

1. **Installation** : Préparation de l'environnement Python.
2. **Tests & Couverture** : Validation du code et génération du rapport XML.
3. **Analyse Radon** : Contrôle de la complexité du code.
4. **Analyse SonarQube** : Envoi des métriques vers le serveur de qualité.
5. **Docker Build** : Création de l'image finale en cas de succès.
