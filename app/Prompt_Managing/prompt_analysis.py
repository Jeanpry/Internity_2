from pydantic import BaseModel
import spacy
# Chargement du modèle SpaCy pour l'anglais
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

class ChatPrompt(BaseModel):
    prompt: str

# Fonction pour extraire les critères du texte en recherchant la séquence spécifique
def extract_criteria(text):
    # Prétraitement du texte
    doc = nlp(text)

    # Initialisation des critères
    type_of_internship = ""
    duration = ""
    place = ""

    # Recherche de la séquence "in the field of"
    for i, token in enumerate(doc):
        if token.text.lower() == "in" and i < len(doc) - 4 and doc[i + 1].text.lower() == "the" and doc[i + 2].text.lower() == "field" and doc[i + 3].text.lower() == "of":
            # Les deux mots suivant la séquence sont considérés comme le type de stage
            type_of_internship = doc[i + 4 : i + 6].text
            break  # Arrête la recherche après avoir trouvé la première occurrence

    # Extraction des entités nommées pour la durée et le lieu (comme précédemment)
    for entity in doc.ents:
        if entity.label_ == "DATE":
            duration = entity.text
        elif entity.label_ == "GPE":
            place = entity.text

    return {
        "Type of Internship": type_of_internship,
        "Duration": duration,
        "Place": place
    }