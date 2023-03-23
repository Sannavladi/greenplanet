import spacy 

nlp = spacy.load("fr_core_news_sm")

def process_text(text):
    doc = nlp(text)
    # Ajouter ici le code pour traiter le texte et retourner une réponse