import requests

# url = "http://localhost:8000/api/users_list/"

# response = requests.get(url)
# print(response.text)

#Get Authentication token 
 
url = "http://localhost:8000/api/auth/"
response = requests.post(url,data = {"username":"pawan","password":"123456789","email":"gp@gmail.com","is_active" : 1})
print(response.text)