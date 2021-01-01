# -*- coding: utf-8 -*-
 
import unittest
import requests

requests.adapters.DEFAULT_RETRIES = 5

def login():
    s = requests.session()
    s.keep_alive = False
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

def addWishlist():
    s = requests.session()
    s.keep_alive = False
    url = "https://dazhadazha.pythonanywhere.com//addWishlist"

    payload={'product_id': '1'}
    files=[

    ]
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def order():
    s = requests.session()
    s.keep_alive = False
    url = "https://dazhadazha.pythonanywhere.com//cart.html"

    payload={'data': '{"products": [{"id": 3, "name": "Digital Camera", "price": 200, "quantity": 3, "sum": 600}, {"id": 2, "name": "Protable Speakers", "price": 200, "quantity": 2, "sum": 400}], "total": 1030, "product_sum": 5}'}
    files=[

    ]
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def register():
    s = requests.session()
    s.keep_alive = False
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

def search():
    s = requests.session()
    s.keep_alive = False
    url = "https://dazhadazha.pythonanywhere.com//search?q=phone"

    payload={}
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def updateCart():
    s = requests.session()
    s.keep_alive = False
    url = "https://dazhadazha.pythonanywhere.com//updateCart"

    payload={'data': '{"products": [{"id": 3, "name": "Digital Camera", "price": 200, "quantity": 3, "sum": 600}, {"id": 2, "name": "Protable Speakers", "price": 200, "quantity": 2, "sum": 400}], "total": 1030, "product_sum": 5}'}
    files=[

    ]
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def resetPassword():
    s = requests.session()
    s.keep_alive = False
    url = "https://dazhadazha.pythonanywhere.com//forget.html"

    payload={'email': 'admin@qq.com',
    'password': 'hahahaha',
    'question': 'What is the name of your pet?',
    'answer': 'katty'}
    files=[

    ]
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


def removeWishlist():
    s = requests.session()
    s.keep_alive = False
    url = "https://dazhadazha.pythonanywhere.com//removeWishlist"

    payload={'product_id': '3'}
    files=[

    ]
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


def addCart():
    s = requests.session()
    s.keep_alive = False
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
 
class TestCase(unittest.TestCase):
 
    def setUp(self):
        print("do something befor test.prepare environment")
 
    def tearDown(self):
        print("do something after test.Clean up")
        
    def test_register(self):
        assert register() == "1"

    def test_login(self):
        assert login() == "1"

    def test_resetPassword(self):
        assert resetPassword() == "1"

    def test_addCart(self):
        assert addCart() == "1"

    def test_addWishlist(self):
        print(addWishlist())

    def test_removeWishlist(self):
        print(removeWishlist())

    def test_search(self):
        print(search())

    def test_updateCart(self):
        print(updateCart())

    def test_order(self):
        assert order() == "1"


 
if __name__ == '__main__':

    unittest.main()