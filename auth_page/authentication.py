user = {}
user_inputs = []
keys = ["name", "email", "password"]

     
def get_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    credentials = [name, email, password]
    user_inputs.append(credentials)


get_user()
print(user_inputs)

# def create_user():
#     i = 0
#     while i < len(keys):
#         user.update({keys[i]: user_inputs[i]})


# if not user:
#     get_user()
#     create_user()


        
print(user)
# print(user_input())
