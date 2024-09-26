# process.py
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    # Use spaCy to process the text
    doc = nlp(text)
    
    # Example: Extracting keywords, intents, etc.
    for token in doc:
        print(f'Token: {token.text}, POS: {token.pos_}, Lemma: {token.lemma_}')
    
    return doc
