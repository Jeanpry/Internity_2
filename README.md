# INTERNITY - Recherche de Stage en Langage Naturel

Ce projet, réalisé par Jean Ponroy et Quentin Goire, étudiants à l'ESIEE Paris en Datascience & Intelligence Artificielle, constitue le premier prototype d'une idée entrepreneuriale. Pendant nos études, nous avons constaté les difficultés liées à la recherche de stages, notamment la fragmentation des plateformes existantes et leurs systèmes de recherche limités. Pour résoudre cela, nous avons conçu une plateforme novatrice permettant une recherche de stage en langage naturel, un véritable chatbot de l'emploi.

## Table des Matières

- [Aperçu](#aperçu)
- [Installation](#installation)
- [Technologies Utilisées](#technologies-utilisées)
- [Fonctionnalités](#fonctionnalités)
- [Utilisation](#utilisation)
- [Remarques et Bilans](#remarques-et-bilan)
- [Auteurs](#auteurs)


## Aperçu

Ce premier prototype propose une fonctionnalité de recherche de stages à partir de requêtes en langage naturel. Il identifie les critères clés des requêtes pour renvoyer les offres correspondantes. Il offre également une recherche par système de filtres classiques.


## Installation

Pour utiliser ce prototype, clonez ce dépôt GitHub :

```bash
git clone <lien_du_repo>
```

Ensuite, lancez le projet avec Docker :
```bash
docker-compose -f docker-compose.yml up
```

Accédez à l'application via votre navigateur à l'URL suivante :
```bash
http://localhost:8080/clean
```

## Technologies Utilisées

Liste des principales technologies/frameworks/langages utilisés dans le projet.

- FastAPI
- Docker
- NLP (spacy)
- SQLALCHEMY

## Fonctionnalités

1. **Recherche en Langage Naturel :** 
   - Saisie de requêtes en langage naturel pour trouver des offres de stage correspondantes.

2. **Filtres Classiques :** 
   - Recherche de stages en utilisant des critères classiques tels que la durée, le lieu et le domaine.

3. **Interface Utilisateur Intuitive :** 
   - Interface conviviale avec des instructions claires pour formuler des requêtes en anglais.

4. **Système de Détail des Offres :** 
   - Affichage des détails des offres de stage correspondant à la requête (entreprise, description du poste, localisation).

5. **Compatibilité Docker :** 
   - Utilisation de Docker pour faciliter le déploiement, assurant la portabilité et la gestion des dépendances.


## Utilisation

Une fois sur l'URL mentionnée, suivez **ces règles** pour formuler vos requêtes :

- Les requêtes doivent être en anglais.
- Spécifiez le lieu, la durée du stage et le domaine recherché.
- La durée du stage s'exprime sous la forme "X Months" avec un "M" majuscule.
- Le domaine se spécifie avec 'in the field of xxx' suivi du domaine recherché, avec une majuscule au début du nom du domaine. 
- Notre base de données ne contient que des offres de stage en Inde, donc les villes sont indiennes.

- **Exemple de requête valide :** *"I'm searching for a 3 Months internship in Delhi, in the field of Photography".*


## Remarques et Bilan 
Ce projet, bien que limité par le temps, a été très stimulant. Il représente un premier pas vers notre ambition. Nous prévoyons de poursuivre son développement.

### Bilan Actuel
L'année chargée que nous sommes entrain de réaliser ne nous a pas permis de développer toutes les fonctionnalités que nous souhaitions. Entre autre, nous aurions beaucoup aimé intégrer un modèle de langage comme GPT-3.5 qui aurait eprmis de construire un vrai assistant dans la recherche de stage. 
Ce projet a cependant été très stimulant et nous a permis de faire un pas de plus vers ce projet qui nous tient beaucoup à coeur, nous avons bien pour but de le continuer ! 

### Futurs Développements
L'intégration d'un modèle de langage afin de créer un vrai copilote de la recherche de stage est primordial pour nous. Un modèle comme celui-ci pourrait nous aider énormément dans la construction de ce projet et pourrait nous permettre de réaliser des fonctionnalités annexes comme la préparation à un entretien en fonction d'une offre donnée, la réalisation de templates de lettres de motivations... 
Aussi, le traitement par langage naturel (NLP)  de la requête utilisateur (assez primaire pour le moment) pourra être grandement amélioré par un modèle de langage puissant. 
C'est pour nous la prochaine grande étape de ce projet et nous espérons avoir l'occasion de la réaliser très vite ! 

## Auteurs

**Quentin Goire & Jean Ponroy** - étudiants ingénieurs ESIEE Paris - Créateurs de la nouvelle technologie révolutionnaire de recherche de stage - *(peut-être) futurs créateurs d'une entreprise au service des étudiants dans la construction de leur profil professionnel*



