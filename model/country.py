import json

def load_db():
    with open ('country_info.json', encoding='utf-8') as mock_database:
        # print(json.load(mock_database))
        return json.load(mock_database)

db = load_db()