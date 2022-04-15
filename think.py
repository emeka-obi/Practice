users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]

# username_mapping = { 'bob': {
#     'id': 1,
#     'username': 'bob',
#     'password':'asdf'
# }
# }

# userid_mapping = {1:{
#     'id':1,
#     'username':'bob',
#     'password': 'asdf

username = 'bob'
user = username_mapping.get(username, None)
print(user.password)
    

