import requests

url = "https://dazhadazha.pythonanywhere.com//register.html"

payload={'email': 'admin@qq.com',
'password': 'adminadmin',
'username': 'admin',
'question': 'What is the name of your pet?',
'answer': 'katty'}
files=[

]
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
