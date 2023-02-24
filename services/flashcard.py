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

def add_flashcard(name: str, color: str):
    init()
    if name != "" and color != "":
        index = len(data['flashcards'])
        data['flashcards'].append({
            "id": shortuuid.uuid(),
            "name": name,
            "color": color,
            "cards": []
        })
        commit()
        return data['flashcards'][index]


def get_all_flashcards() -> list:
    init()
    return data['flashcards']

def get_by_flashcards_name(name: str) -> list:
    init()
    if name == "":
        return data['flashcards']
    return [f for f in data.get('flashcards') if name.lower() in f.get("name").lower()]

def get_flashcard_by_id(id: str):
    init()
    flashcard = list(filter(lambda f: f['id'] == id, data['flashcards']))[0]
    return flashcard
    
def update_flashcard_by_id(id: str, name: str = None, color: str = None):
    init()
    flashcard_index = [id in f['id'] for f in data['flashcards']].index(True)
    if name != None:
        data['flashcards'][flashcard_index]["name"] = name

    if color != None:
        data['flashcards'][flashcard_index]["color"] = color

    commit()
    return data['flashcards'][flashcard_index]

def delete_flashcard_by_id(id: str):
    init()
    data['flashcards'] = [f for f in data.get('flashcards') if f.get("id") != id]
    commit()



    
