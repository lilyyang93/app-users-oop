class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
    
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nUsername: {self.username}\nEmail: {self.email}"
    
user1 = User('Lily', 'Yang', 'lilyyang', 'lilyyang@email.com')
user2 = User('Alex', 'Song', 'alexsong', 'alexsong@email.com')
user3 = User('Mamba', 'Song', 'mambasong', 'mambasong@dog.com')

print(user1)
print(user2)
print(user3)
