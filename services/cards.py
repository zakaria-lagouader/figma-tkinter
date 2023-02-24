import json
import shortuuid

data = None

with open("db.json", "r") as db:
    data = json.load(db)

def init():
    global data
    with open("db.json", "r") as db:
        data = json.load(db)

def commit():
    with open("db.json", "w") as file:
        json.dump(data, file)

def get_flashcard_index(id: str):
    init()
    flashcard_index = [id in f['id'] for f in data['flashcards']].index(True)
    return flashcard_index

def add_card(flashcard_id:str, word: str, translation: str):
    init()
    flashcard_index = get_flashcard_index(flashcard_id)
    card_index = len(data['flashcards'][flashcard_index]["cards"])
    data['flashcards'][flashcard_index]["cards"].append({
        "id": shortuuid.uuid(),
        "word": word,
        "translation": translation,
    })
    commit()
    return data['flashcards'][flashcard_index]["cards"][card_index]

def get_cards(flashcard_id:str):
    init()
    flashcard_index = get_flashcard_index(flashcard_id)
    return data['flashcards'][flashcard_index]["cards"]

def get_card_index(flashcard_id:str, id: str):
    init()
    flashcard_index = get_flashcard_index(flashcard_id)
    card_index = [id in c['id'] for c in data['flashcards'][flashcard_index]["cards"]].index(True)
    return flashcard_index, card_index

def get_card_by_id(flashcard_id:str, id: str):
    init()
    flashcard_index, card_index = get_card_index(flashcard_id, id)
    return data['flashcards'][flashcard_index]["cards"][card_index]

def update_card_by_id(flashcard_id:str, id: str, word: str = None, translation: str = None):
    init()
    flashcard_index, card_index = get_card_index(flashcard_id, id)
    
    if word != None:
        data['flashcards'][flashcard_index]["cards"][card_index]["word"] = word
    if translation != None:
        data['flashcards'][flashcard_index]["cards"][card_index]["translation"] = translation

    commit()
    data['flashcards'][flashcard_index]["cards"][card_index]

def delete_card_by_id(flashcard_id:str, id: str):
    init()
    flashcard_index = get_flashcard_index(flashcard_id)
    data['flashcards'][flashcard_index]["cards"] = [c for c in data['flashcards'][flashcard_index]["cards"] if c.get("id") != id]
    commit()



    
