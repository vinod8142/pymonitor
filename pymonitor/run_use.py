# import requests
# import json
# import pdb

# migrate first
# create asuper user through terminal then follow below process
# r = requests.post("http://127.0.0.1:8000/login/", data={'username': 'vinod', 'password': 'admin123'})
# token = json.loads(r.text)['token']

############ to register
# r = requests.post("http://127.0.0.1:8000/users_info/", 
#     data={'username': 'vinod', 
#         'password': 'admin123', 
#         'email':'test@gmail.com',
#         'fname':'Vinod',
#         'lname':'Kopperla',
#         'mobile':'8142832767',
#         'hometown':'Anantapur'},headers={'Authorization': 'Token {}'.format(token)})

############to get all users data
# result = requests.get("http://127.0.0.1:8000/users_info/", 
#     headers={'Authorization': 'Token {}'.format(token)})
# print(result.text) 

############## to get user data

# result = requests.get("http://127.0.0.1:8000/users_info/siva", 
#     headers={'Authorization': 'Token {}'.format(token)})
# print(json.loads(result.text))

# r = requests.put("http://127.0.0.1:8000/users_info/vinod/", 
#     data={'username': 'vinod', 
#         'password': 'admin123', 
#         'email':'vinod@gmail.com',
#         'fname':'Vinod Kumar',
#         'lname':'K',
#         'mobile':'1234567',
#         'hometown':'Anantapur'},headers={'Authorization': 'Token {}'.format(token)})
# print(r.text)

##############to delete
# r = requests.delete("http://127.0.0.1:8000/users_info/vinod", 
#     headers={'Authorization': 'Token {}'.format(token)})
# print(r.text)

############# to get all  general_info
# result = requests.get("http://127.0.0.1:8000/general_info/", 
#     headers={'Authorization': 'Token {}'.format(token)})
# print(result.text) 
############## to get specific server info
# result = requests.get("http://127.0.0.1:8000/general_info/192_168_64_132", 
#     headers={'Authorization': 'Token {}'.format(token)})
# print(result.text)

############### to get all servers performance
# result = requests.get("http://127.0.0.1:8000/performance_info/", 
#     headers={'Authorization': 'Token {}'.format(token)})
# print(result.text)

############## to get specifc server performance 
# result = requests.get("http://127.0.0.1:8000/performance_info/192_168_64_132", 
#     headers={'Authorization': 'Token {}'.format(token)})
# print(result.text)
