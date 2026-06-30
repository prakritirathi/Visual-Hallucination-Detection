from utils import extract_objects
import json
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Read caption
with open("output/caption.json", "r") as f:
    data = json.load(f)

caption = data["caption"]

print("Caption:")
print(caption)
print("\n-------------------------")

# Process caption
doc = nlp(caption)

# Print token information
for token in doc:
    print(
        f"{token.text:15} "
        f"POS={token.pos_:10} "
        f"DEP={token.dep_:15} "
        f"HEAD={token.head.text}"
    )
    
print("\nObjects Found:")
print("----------------")

objects = extract_objects(doc)

claims = []

for obj in objects:
    claims.append({
        "type": "object",
        "value": obj
    })
    
import os

os.makedirs("output", exist_ok=True)

with open("output/claims.json", "w") as f:
    json.dump(claims, f, indent=4)

print("claims.json created successfully!")