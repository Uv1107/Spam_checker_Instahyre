## How to run this app
* Firstly create an environment and install these dependencies (you can also run it without making an environment).
  * django
  * djangorestframework
  * djangorestframework-simplejwt
* Make sure you are in the `spam-checker` folder

~~~
spam_checker/    ⬅️ **This folder**
├── spam_checker/          
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        
│   ├── urls.py           
│   └── wsgi.py
├── app/                   
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/       
│   ├── models.py          
│   ├── serializers.py     
│   ├── tests.py
│   ├── urls.py           
│   └── views.py           
├── db.sqlite3            
├── manage.py             
└── requirements.txt
~~~
* Open the terminal and enter `python manage.py runserver`, the server will start running on port `8000` (default). You can also change the port number by entiring `python manage.py runsurver <PORT_NUMBER>`
* If you encounter any error make sure to run `python manage.py makemigrations` and `python manage.py migrate`, to check if everything is running as expected.


## API ENDPOINTS
1) ### Register
   * Endpoint: `/api/register/`
   * Method: `POST`
   * Description: Register a new user with username, email, and phone number.
    #### cURL Command: 
~~~ 
curl -X POST http://127.0.0.1:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{
  "username": "jack_doe",
  "email": "jack@example.com",
  "phone_number": "999999999",
  "password": "password999"
}'
~~~

2) ### Login
   * Endpoint: `/api/login/`
   * Method: `POST`
   * Description:  Logs in a user and returns a JWT token for authentication.
    #### cURL Command: 
~~~ 
curl -X POST http://127.0.0.1:8000/api/login/ \
-H "Content-Type: application/json" \
-d '{
  "username": "jack_doe",
  "password": "password999"
}'
~~~


3) ### Mark Spam
   * Endpoint: `/api/report-spam/`
   * Method: `POST`
   * Description:  Marks a phone number as spam. Requires authentication.
   * Authorization: `Bearer <access_token>` (you will get access_token from the login response)
    #### cURL Command: 
~~~ 
curl -X POST http://127.0.0.1:8000/api/report-spam/ \
-H "Authorization: Bearer access_token_here" \
-H "Content-Type: application/json" \
-d '{
  "phone_number": "9876543210",
  "is_spam": true
}'
~~~

4) ### Search by Name
   * Endpoint: `/api/search/?query=<name>&type=name`
   * Method: `GET`
   * Description:   Search for users by name. Results include name, phone number, and spam likelihood. Requires authentication.
   * Authorization: `Bearer <access_token>` (you will get access_token from the login response)
    #### cURL Command: 
~~~ 
curl -X GET "http://127.0.0.1:8000/api/search/?query=john&type=name" \
-H "Authorization: Bearer access_token_here"
~~~

5) ### Search by PhoneNumber
   * Endpoint: `/api/search/?query=<phone_number>&type=phone`
   * Method: `GET`
   * Description:   Search for a user by phone number. Requires authentication.
   * Authorization: `Bearer <access_token>` (you will get access_token from the login response)
    #### cURL Command: 
~~~ 
curl -X GET "http://127.0.0.1:8000/api/search/?query=1234567890&type=phone" \
-H "Authorization: Bearer access_token_here"
~~~
  