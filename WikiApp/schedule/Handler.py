import json

def load_file():
    with open('schedule/jsonFiles/json_raw_data.json', 'r', encoding='utf8') as jf:
        data = json.load(jf)
        return data

def get_first_date():
    data = load_file()
    a = set()
    for x in data:
        a.add(x['data'])
    return sorted(a)

def get_form():
    data = load_file()
    a = set()
    for x in data:
        a.add(x['formaStudiow'])
    return sorted(a)

def get_degree():
    data = load_file()
    a = set()
    for x in data:
        a.add(x['stopien'])
    return sorted(a)

def get_year():
    data = load_file()
    a = set()
    for x in data:
        a.add(x['semestr'])
    return sorted(a)

def get_specialty():
    data = load_file()
    a = set()
    for x in data:
        a.add(x['grupa'])
    return sorted(a)

def get_group(semestr):
    data = load_file()
    a = set()
    for x in data:
        if x['semestr'] == semestr:
            a.add(x['grupa'])
    return sorted(a)