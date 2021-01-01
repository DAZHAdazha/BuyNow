import requests

url = "https://dazhadazha.pythonanywhere.com//wishlist.html"

payload={'product_id': '1',
'product_quantity': '2'}
files=[

]
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
