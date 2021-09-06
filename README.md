[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# LevequeBenjamin_P12_28082021

## Développez une architecture back-end sécurisée en utilisant Django ORM

Le projet 10 de la formation Développeur d'application Python est le développement d'une architecture back-end sécurisée
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

### Usage

Pour lancer l'application utilisez la commande:

```
$ python manage.py runserver
```
