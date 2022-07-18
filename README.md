# flask-resful-store
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
## First needs to create user 
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
## If u need to create product in store
```
/admin/<product>
methods: POST
```
## To check docs
```
/api/docs
methods: GET
```
