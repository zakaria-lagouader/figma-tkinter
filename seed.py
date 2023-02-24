from services import flashcard, cards
import pandas as pd
import re

df = pd.read_csv("frToEng.csv")
# Detect and remove incomprehensible words
def filter(s):
    if type(s) is not str:
        return True
    else:
        if re.findall("[^a-zA-Z0-9\s?'-,]", s):
            return False
        else: 
            return True

df = df[df["French"].apply(filter)].reset_index(drop=True)
df = df[df["English"].apply(filter)].reset_index(drop=True)

fc = flashcard.add_flashcard("English", "#ff8080")

for index, row in df.iterrows():
    card = cards.add_card(
        flashcard_id=fc["id"],
        word=row["French"],
        translation=row["English"]
    )


print("DB Seeded Successfully !")

