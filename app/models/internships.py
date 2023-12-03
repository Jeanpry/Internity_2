import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models.database import SQLALCHEMY_DATABASE_URL
from importers.csv_import import Internships # Assurez-vous d'importer votre modèle ici
from models.database import BaseSQL

# Configuration de la connexion à la base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL)
try:
    # Tente de se connecter à la base de données
    engine.connect()
    print("Connexion à la base de données réussie.")
except Exception as e:
    print("Erreur lors de la connexion à la base de données : ", e)

Session = sessionmaker(bind=engine)

inspector = inspect(engine)

BaseSQL.metadata.create_all(engine)

if 'internships' in inspector.get_table_names():
    print("La table 'internships' existe.")
else:
    print("La table 'internships' n'existe pas.")

# Lecture du fichier CSV
df = pd.read_csv('Internship.csv')

# Insertion des données dans la base de données
session = Session()
for index, row in df.iterrows():
    internship = Internships(
        id=index,
        actively_hiring=row['actively_hiring'],
        Type_of_internship=row['Type_of_internship'],
        company_name=row['company_name'],
        location=row['location'],
        stipend=row['stipend'],
        duration=row['duration'],
    )
    session.add(internship)

session.commit()
session.close()


