# CRM Epic Events

CRM Epic Events est un système de gestion de la relation client (CRM) développé pour répondre aux besoins spécifiques d'Epic Events, une entreprise de conseil et de gestion dans l'événementiel.

Ce système permet à Epic Events de collecter, stocker et gérer de manière sécurisée les informations sur ses clients, ainsi que les contrats et les événements qu'elle organise.

## Fonctionnalités

- **Gestion des clients**: Permet de créer, afficher, mettre à jour et supprimer des clients.
- **Gestion des contrats**: Permet de créer, afficher, mettre à jour et supprimer des contrats.
- **Gestion des événements**: Permet de créer, afficher, mettre à jour et supprimer des événements.
- **Authentification et autorisation**: Utilise l'authentification basée sur les jetons JWT pour sécuriser l'accès aux fonctionnalités du CRM. Les utilisateurs doivent être authentifiés et avoir les autorisations appropriées pour effectuer des actions.

## Technologies utilisées

- **Django**: Framework web utilisé pour le développement de l'application.
- **Python**: Langage de programmation principal utilisé.
- **JWT (JSON Web Tokens)**: Utilisé pour l'authentification des utilisateurs.
- **Sentry**: Utilisé pour la journalisation et la surveillance des erreurs.

## Configuration requise

- Python 3.x
- Django
- python-dotenv

## Installation

1. Cloner le repository GitHub :
   ```
   git clone https://github.com/votre-utilisateur/crm-epic-events.git
   ```

2. Installer les dépendances :
   ```
   pip install -r requirements.txt
   ```

3. Créer et configurer le fichier `.env` avec les informations requises (clé secrète, informations de base de données, etc.).

4. Appliquer les migrations de la base de données :
   ```
   python manage.py migrate
   ```

5. Lancer le serveur de développement :
   ```
   python manage.py runserver
   ```

6. Accéder à l'application dans votre navigateur à l'adresse `http://localhost:8000`.

Voici comment vous pouvez ajouter ces informations dans le README :

## Authentification

Pour vous connecter à l'application, vous devez fournir un nom d'utilisateur (username) et un mot de passe (password) dans un fichier `.env`. Utilisez les identifiants suivants pour vous connecter en tant qu'utilisateur existant :

- **Support_admin**:
  - Username: Support_admin
  - Mot de passe: admin
- **Gestion_admin**:
  - Username: Gestion_admin
  - Mot de passe: admin
- **Commercial_admin**:
  - Username: Commercial_admin
  - Mot de passe: admin

Pour obtenir un jeton JWT après vous être connecté, utilisez la commande suivante :

```
python manage.py login
```

Le jeton JWT sera généré et enregistré dans un fichier `jwt_token.txt`. Ce jeton sera utilisé pour authentifier les requêtes aux autres fonctionnalités de l'application. Assurez-vous que le fichier `.env` contenant les informations d'identification est correctement configuré avant d'utiliser cette commande.

Pour plus d'informations sur l'authentification et l'utilisation du jeton JWT, veuillez consulter la section correspondante dans ce README.

## Commandes

Après vous être connecté, vous pourrez utiliser ces commandes. Cependant, veuillez noter que certaines commandes ne sont disponibles qu'avec un compte spécifique. Par exemple, la commande 'create_collaborator' n'est utilisable que par l'équipe de gestion d'Epic Events :

D'accord, voici la liste de commandes avec chaque commande mise en forme dans des balises de code (```) pour le fichier README :


### [contracts]
```
create_contract
```
```
delete_contract
```
```
show_contract_detail
```
```
show_contracts_list
```
```
update_contract
```

### [events]

```
create_event
```
```
show_event_detail
```
```
show_events_list
```
```
update_event
```


### [users]

```
create_client
```
```
create_collaborator
```
```
delete_client
```
```
delete_collaborator
```
```
login
```
```
logout
```
```
show_client_detail
```
```
show_clients_list
```
```
show_collaborator_detail
```
```
show_collaborators_list
```
```
update_client
```
```
update_collaborator
```


## Diagramme

![diagramme uml](/img/UML.png)

## Sentry
![screen sentry](/img/Screen_sentry_P12.png)