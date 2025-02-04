## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/oussamaabid82/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Prérequis

- [Avoir un compte sur Docker Hub](https://hub.docker.com/)
- [Avoir Docker sur l'ordinateur](https://www.docker.com/get-started/)
- [Avoir un compte circleCI](https://circleci.com/)
- [Avoir un compte Heroku](https://signup.heroku.com/)
- [Avoir Heroku sur l'ordinateur](https://devcenter.heroku.com/articles/heroku-cli)
- [Avoir un compte SENTRY](https://sentry.io/auth/login/)


### Résumé du fonctionnement
Dès qu'on pousse un commit sur GitHub, circleCI se charge de le tester et si tous les tests passe bien circleCI passe le commit à Docker Hub pour créer le conteneur ensuite Heroku le récupère pour le rendre accessible.

### Étapes de configuration

#### 1. Docker hub

Après la création d'un compte docker hub, utilisez le bouton ```Create Repository``` pour créer un nouveau dépot pour les conteneurs.

Les variables suivantes seront utiles pour la configuration de CircleCI :

- DOCKER_LOGIN (Identifiant Docker-Hub)
- DOCKER_PASSWORD (Mot de passe Docker-Hub)

Pour créer un container et lancer une image en local:
Récupérer le dernier commit de hachage en tapant dans le terminal:
```git rev-parse HEAD```
> ```docker run -p 127.0.0.1:8000:8000 DOCKER_LOGIN/IMAGE_NAME:le dernier commit de hachage```

#### 2. Heroku

Après la création d'un compte [Heroku](https://signup.heroku.com/), utilisez le menu ```New / Create new app``` pour créer une nouvelle application (essayez de nommer l'application "oc-lettings" ou quelque chose similaire)

Dans le nouveau app utilisez le bouton ```Deploy``` puis dans le menu ```Deployement method``` utilisez ```Container Registry``` et suivez la documentation

#### 3. CircleCI

Après la création d'un compte, utilisez le menu ``Projets`` puis connectez le repo-github avec lequel vous travaillez à l'aide du bouton ``Set Up Project``.
Utilisez le bouton ```...``` puis ``Project Settings``, puis ``Environment Variables`` à gauche.
Placez les variables suivantes :

- HEROKU_APP_NAME
> Le nom de l'application Heroku

- HEROKU_API_KEY
> Utilisez heroku authorizations:create de Heroku-CLI (Token)

- DOCKER_LOGIN
> Votre identifiant Docker-Hub

- DOCKER_PASSWORD
> Votre mot de passe Docker-Hub

- IMAGE_NAME
> Le nom de l'image Docker

- SENTRY_DSN
> Vous pouvez la trouver sur le site Sentry dans Settings / Projects / {VOTRE_PROJECT} / Client Keys (DSN) / DSN

- DJANGO_SECRET_KEY
> Clé Django

#### 4. Sentry

Après la création d'un compte, utilisez le bouton ``Create Project``
- Choose a platform: choisissez Django
- Give your project a name: choisissez un nom
- utilisez le bouton ```Create Project``` 
