[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# LevequeBenjamin_P12_28082021

## Développez une architecture back-end sécurisée en utilisant Django ORM

Le projet 12 de la formation Développeur d'application Python est le développement d'une architecture back-end sécurisée
en utilisant Django ORM.

## Documentation Postman

Vous trouverez une documentation détaillée de l'api en suivant ce [lien](https://documenter.getpostman.com/view/14483216/U16gPnFv).

## Technologies
- Python
- Django rest_framework
- django-rest-auth
- djangorestframework-simplejwt

## Auteur
Lévêque Benjamin

### Installation

Cet application web exécutable localement peut être installée en suivant les étapes décrites ci-dessous.

#### 1. Clonez le [repository](https://github.com/LevequeBenjamin/LevequeBenjamin_P12_28082021.git) à l'aide de la commande suivante :

```
$ git clone "https://github.com/LevequeBenjamin/LevequeBenjamin_P12_28082021.git"
``` 
(vous pouvez également télécharger le code en temps
[qu'archive zip](https://github.com/LevequeBenjamin/LevequeBenjamin_P12_28082021/archive/refs/heads/master.zip))

#### 2. Créez un fichier `.env` à la racine du dossier `django_rest_epic_events`et créez vos variables d'environnement.

```
SECRET_KEY = 'django-insecure-ubq*h$699uyj-)0svi1i&o-7bwdk8kh&g&u@(w^p8%9c4o%xqv'
DEBUG=True
ALLOWED_HOSTS='127.0.0.1'
CORS_ALLOWED_ORIGINS = 'http://localhost:8000'
PSQL_NAME="epic_events"
PSQL_USER="epic_events"
PSQL_PASSWORD="epic_events"
PSQL_HOST="localhost"
PSQL_PORT="5432"
```

#### 3. Exécutez l'application dans un environnement virtuel

Rendez-vous depuis un terminal à la racine du répertoire BenjaminLeveque_P12_28082021/ avec la commande :
```
$ cd BenjaminLeveque_P12_28082021/
```

Pour créez un environnement, utilisez la commande :

`$ python3 -m venv env` sous macos ou linux.

`$ python -m venv env` sous windows.

Pour activer l'environnement, exécutez la commande :

`$ source env/bin/activate` sous macos ou linux.

`$ env/Scripts/activate` sous windows.

#### 4. Installez les dépendances du projet avec la commande:
```
$ pip install -r requirements.txt
```

#### 5. Créez une base de données POSTGRESQL :
Assurez-vous que postgreSQL est disponible sur votre système.
Vous trouverez une documentation détaillée de PostgreSQL en suivant ce [lien](https://www.postgresql.org/).

Dans psql CLI, tapez (si vous modifiez la valeur ci-dessous, modifiez également .env):
```
CREATE DATABASE epic_events;
CREATE USER epic_events WITH PASSWORD 'epic_events';
ALTER USER epic_events CREATEDB;
ALTER ROLE epic_events SET client_encoding TO 'utf8';
ALTER ROLE epic_events SET default_transaction_isolation TO 'read committed';
ALTER ROLE epic_events SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE epic_events TO epic_events;
\q
```
### Usage

Créez un super utilisateur :

```
$ python manage.py createsuperuser
```

Pour lancer l'application utilisez la commande:

```
$ python manage.py runserver
```

### Tests

#### 1. Testez l'api avec la commande :
```
$ python manage.py test
```
#### 2. Générez un rapport de couverture avec les commandes:
```
$ coverage run --source='.' manage.py test accounts clients contracts events
$ coverage report
```

Puis rendez-vous sur `127.0.0.1:8000/management/` et connectez vous avec les identifiants de votre super utilisateur.
Pour l'utilisation des points de terminaisons de l'api veuillez suivre la [documentation Postman](https://documenter.getpostman.com/view/14483216/U16gPnFv).
