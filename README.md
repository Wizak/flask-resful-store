# flask-resful-store
## Video Instruction For Use
```
https://user-images.githubusercontent.com/66076836/179434436-11b48696-f2a4-4556-8fd0-e364b98086db.mp4

```
---
## Setting Virtual Environment for Python3.6
```
virtualenv --python="/usr/bin/python3.6"
venv\Scripts\Activate
```
---
## Install Dependency
```
pip install -r requirements.txt
```
## Run Server
```
python run.py
```
---
## First need to create user 
```
/user/
methods: POST
```
### Request Data
```Json
{
  "username": "username_example",
  "password": "pass_example"
}
```
---
## Next need to login
```
/user/login
methods: POST
```
### Request Data
```Json
{
  "username": "username_example",
  "password": "pass_example"
}
```
### Response Data
```Json
{
  "access-token": "token_example"
}
```
---
## If you are signed in, u can check/update user account, users
```
/user/account 
methods: GET, PUT, DELETE

/users/<username>
mwthods: GET
```
---
## To add product to cart
```
/store/
methods: GET

/store/cart
methods: GET

/store/cart/<product>
methods: POST, DELETE
```
---
## If u need to create product to store
```
/admin/<product>
methods: POST
```
## To check docs
```
/api/docs
methods: GET
```
