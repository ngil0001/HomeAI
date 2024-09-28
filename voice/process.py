# process.py
import spacy
from spacy.matcher import Matcher

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)
# Define the patterns
patterns = [
     {"label": "ACTION", "pattern": [{"LOWER": "turn"}, {"LOWER": "on"}]},
    {"label": "ACTION", "pattern": [{"LOWER": "turn"}, {"LOWER": "off"}]},
    {"label": "DEVICE", "pattern": [{"LOWER": "lights"}]},
    {"label": "LOCATION", "pattern": [{"LOWER": "kitchen"}]},
    {"label": "LOCATION", "pattern": [{"LOWER": "living"}, {"LOWER": "room"}]}
]

for pattern in patterns:
    matcher.add(pattern["label"], [pattern["pattern"]])

def process_text(text):
    # Use spaCy to process the text
    doc = nlp(text)
    
    # Use the matcher to find matches in the doc
    matches = matcher(doc)
    
    # Extract the matched entities
    entities = {}
    for match_id, start, end in matches:
        label = nlp.vocab.strings[match_id]
        span = doc[start:end]
        entities[label] = span.text

    return entities
