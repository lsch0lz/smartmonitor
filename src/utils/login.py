import json

def check_login(username, password):
    with open('data/credentials.json') as f:
        data = json.load(f)
        
        if username == data['username'] and password == data['password']:
            return True
        else: 
            return False

