# Documentation Django et Docker.

## List des chemins d'url

Access a l'application public : 
* Index :  http://127.0.0.1:8002/
* Livres : http://127.0.0.1:8002/livres/
* Categories : http://127.0.0.1:8002/categories/
* Auteurs : http://127.0.0.1:8002/auteurs/

Access a l'application api : 
    
Auteurs:
* list et ajout d'auteur : http://127.0.0.1:8002/api/auteurs/
* modification et supression d'auteurs : http://127.0.0.1:8002/api/auteurs/livres/<int:id_auteur>/

Livres:
* list et ajout de livres : http://127.0.0.1:8002/api/livres/
* modification et supression de livres : http://127.0.0.1:8002/api/livres/livres/<int:id_livre>/


## Fonctionnement de Django

1. Apres avoir créer l'application public, on doit ensuite creer les vues dans Django/public/views.py en important le model du bases de données et en ajoutant une fonction 'index'. Ensuite on doit ajouter dans le fichier Django/public/urls.py une définition de chemin pour redirectionner les requete vers l'index par le url /. On creer enfin dans /Django/public/templates/index.html pour le mise en page du site web.

2. Dans le fichier setting.py du repertoire principale de notre repertoire projet que on doit modifier pour spécifier le répertoire qu'on souhaite utiliser pour notre application. C'est ainsi dans la section : "DATABASES"

3. C'est le fichier setting.py, le reste wsg.py, manage.py, je n'ai pas pu les utiliser, c'est fait pour la prod.

4. python manage.py makemigrations n'a pas d'éffet a part créer un fichier .py qui va permettre d'appliquer une création de shéma ou un mise a jour d'un shema du base de données utilisé par l'application. Le shema ou model du base de données est defini dans models.py. python manage.py migrate permet d'appliquer le changement de structure de base de données definie par la commande makemigrations.
Les fichiers mise en oeuvres pendant ces exécutions sont : 
    - settings.py pour spécifier la base de données.
    - models.py pour spécifier le "model" ou le shéma de la base de données.
    - manage.py, pour lancer les commandes de migrations.  

## Fonctionnement de Docker

1. 
* FROM : l'options qui permet de spécifier l'image d'un container qu'on veut télécharger de Docker Hub pour build notre container.

* RUN : L'options qui permet d'executer les commandes dans le container Docker pendant sa construction, c'est a dire avant son démarrage, qui a souvent pour but de télécharger en amont les dépendance ou de configurer les fichier essentiel au lancement de l'application. 

* WORKDIR : Option qui permet de définir le répertoire de travail par défaut du container dans laquelle touts les future commande ou manipulation de fichiers seront éffectuer. 

* EXPOSE : L'option qui permet de spécifier les ports sur laquelle va écouter le container une fois lancé.

* CMD : L'option qui permet de spécifier la commande par défaut lorsque le conteneur est lancé. 

2.
ports:
    - "80:80" : Cette commande permet de mapper le port qu'écoute le container dans son réseaux avec celle de la machine hote. 

build: 
    context: .
    dockerfile: Dockerfile.api : cette options permet de spécifier à docker compose le répertoire et le fichier Dockerfile auxquelle elle doit se référencer pour construire son container. 

depends_on:
    - web
    - api : 
    Cette option permet de spécifier les services out containers auquelle va dépendre une container pour pouvoir se lancer.

environment:
    POSTGRES_DB: $POSTGRES_DB
    POSTGRES_USER: $POSTGRES_USER
    POSTGRES_PASSWORD: $POSTGRES_PASSWORD
    : Cette options permet de spécifier les variables d'environnements. Dans ce cas ces options petmet de spécifier les informations concernant la base de données. Ces variable d'environnement pourait etre créer par la commande export. 

3. On peut definir des variables d'environnement dans un container en specifiant la variable ENV dans le Dockerfile.

4. On peut spécifier directement le nom du container web dans le fichier nginx.conf de nginx. Nginx va résoudre automatiquement grace au service dns interne de docker. 
