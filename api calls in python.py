
#THIS IS API EXTERNAL CONNECTION WORK 
import requests 

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()
print(data)


#print (data["address"])
print(data["address"]["city"])
print(data["name"])
print(data["id"])
print(data["email"])