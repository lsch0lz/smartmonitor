import json

def create_user(username, password):
    with open('data/credentials.json', 'r') as f:
        data = json.load(f)

    data['username'] = username
    data['password'] = password

    with open('data/credentials.json', 'w') as j:
        json.dump(data, j)
    return True
