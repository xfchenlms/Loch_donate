# Solo assignment
## Description

### Render URL: https://loch-donate.onrender.com/
Some of the features in the project require superuser permissions to be used. If you need to, you can create them with the following code:
  
    python3 manage.py creatsuperuser
    
You can also log in directly using the super administrator account that I have created
#### username: xiaofanlms
#### password: 123456ABCabc

# instructions
## Configuring the development environment
Before you start working with the code, you need to configure your environment.
    
    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
    
I use Django (https://www.djangoproject.com) as my web framework for the application. So install that with

     pip install django

And a library for displaying css styles

    pip install whitenoise
    
## migrate data
Then we need to do data migration in order to use the site properly.

    python3 manage.py makemigrations
    python3 manage.py migrate
  
    
 ## Start going to the website
We do this using the manage.py command tool by entering this command in the terminal:

    python3 manage.py runserver

If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):

    python3 manage.py runserver 0.0.0.0:8000 

If it went well, then you should have reached the homepage of the website.

## Website function introduction
#### Go to the home page
By clicking on the View Lochs button, a user can be directed to the web page of product list

#### Enter product list
The product list shows lochs in Scotland and initial information of the lochs including prices, and hyperlinks directing users to the details of lochs and web page for donating

#### Start shopping
By clicking on the donate button, a user can start shopping (donating to) a loch. The user needs to log in to start shopping.

#### Confirming donation and check out
On the donation page, the user can put a loch in the "cart", and confirming the donation

#### Administrator, guest and user
Different levels of access such as administrator, user and guest are provided, where administrator can manage users and orders, guest can browse the site, and user can place order to donate after logging in 







    

