# Caller Info

Steps to run the API
## Install dependencies
```
pip3 install requirements.txt
```


##Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```



## Create Sample Data

```
python manage.py shell
from main.create_sample_data import *
create_users()
create_contacts()
```

## Runserver
```
python3 manage.py runserver
```

## Test the API

```
Route: http://localhost:8000/api/v1/auth/login/
Request Type: POST
Data: 

    {
        "number":"1234567890",
        "password":"test"
    }
```
```
Route: http://localhost:8000/api/v1/users/
Request Type: GET
Data: 

    {
        "username":"test",
        "name":"test",
        "phone":"1234567890",
        "email":"test@test.com",
    }
```

### To view all your contacts 
```
Public Route: http://localhost:8000/api/v1/users/<user_id>/contacts/
Request Type: GET
```

### To list or add a contact as SPAM
```
Private Route: http://localhost:8000/api/v1/users/<user_id>/spam_contacts/
Request Type: GET, POST
Data:
    {
        "name":"spam",
        "phone": "9876543210"
    }
```

### To search a contact by name
```
Private Route: http://localhost:8000/api/v1/users/search?name=cotact
Request Type: GET
```

### To search a contact by number
```
Private Route: http://localhost:8000/api/v1/users/search?number=8887655679
Request Type: GET
```
