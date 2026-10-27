user = {}

keys = ["name", "email", "password"]

name = input("Enter name: ")
email = input("Enter email: ")
password = input("Enter password: ")

user_inputs = [name, email, password]
   
     
i = 0
while i < len(keys):
    user.update({keys[i]: user_inputs[i]})
    i += 1

print(user)
    

# print(user_input())

# def create_user(name, email, password):
#     if user != None:
#         user = {
#             "name": name,
#             "email": email,
#             "password": password
#         }