# financeTracker

### How to use the backend
#### Clone the repo
`git glone https://github.com/mohamedAbdelaleem/financeTracker.git`
#### Navigate to the project folder
`cd financeTracker\`
#### Option 1: Use pipenv to install the dependencies
`pip install pipenv`
activate the virtual environment
`pipenv shell`
install the dependencies
`pipenv install`

#### Option 2: Install the dependencies from requirements.txt
`pip install -r requirements.txt`

#### Run the local server
`python src\manage.py runserver`

### Auth endpoints

#### Login
`http://127.0.0.1:8000/api/auth/login`
it accepts email and password in JSON format
for example:
```
{
    "email": "mo@test.com",
    "password": "123"
}
```
#### Signup
`http://127.0.0.1:8000/api/auth/signup`
it accepts: email, first_name, second_name, password, and confirmed_password in JSON format
for example:
```
{
    "email": "mo@test.com",
    "first_name": "hamo",
    "second_name": "abdo",
    "password": "123",
    "confirmed_password": "123"
}
```

#### Logout
`http://127.0.0.1:8000/api/auth/logout`
The request should include `Authorization` header with a `Token`
for example: 
`Authorization: Token 32c32faffaaf9ab57f46c3cf2b7e1bbf16bbdaae6e26d48dbb87fd557a6ed13c`


