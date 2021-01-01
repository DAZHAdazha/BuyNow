import requests

url = "https://dazhadazha.pythonanywhere.com//login.html"

payload={'email': 'admin@qq.com',
'password': 'hahahaha',
'remember': 'false'}
files=[

]
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
