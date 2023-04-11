import requests


class My_User:
    def __init__(self, id, email, username, name):
        self.id = id
        self.email = email
        self.username = username
        self.name = name

    def __str__(self):
        return f"id: {self.id}, email: {self.email}, username: {self.username}, name: {self.name}"


def find_user(name):
    url = 'https://jsonplaceholder.typicode.com/users'
    res = requests.get(url)
    users = res.json()

    for user in users:
        if user['name'] == name:
            my_user = My_User(user['id'], user['email'], user['username'], user['name'])
            return my_user

    return 'User not found.'


name = input('Enter user name: ')
user = find_user(name)
print(user)

