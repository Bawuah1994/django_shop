# Shopping with Django
A shopping site done in Django to show the basics of an ecommerce site. This is a remake of an older application, which tried to do too much. This one focuses on the shopping part, with support for testing.

After you clone or download the repository use these commands to set things up and note that python3 and python works the same if configured correctly. If you have issues, you can use python3 instead of python.:

    pyenv local 3.10.7 # this sets the local version of python to 3.10.7
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment, this is for linux and mac
    .venv\Scripts\activate # this activates the virtual environment, this is for windows
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.    
    pip install django
    pip install faker
    python manage.py migrate
    
   
This app uses Faker to generate customer and product details in the 'shop/management/commands/populate_tables.py' file. Go to https://faker.readthedocs.io/en/stable/providers.html and look through the options for Standard Providers to see if you want to change any details in values used.

You should now be able to populate the tables with the command:

        python manage.py populate_tables

Then you can start the server to see it running. 

You will need to create a superuser as well if you want to work with the admin features. You can do that with the command:

        python manage.py createsuperuser

You will need to pass the csv file of the open dataset as well if you want to work with the data from it. You can do that with the command:

        python manage.py parse_csv

Sometimes you will need to clear all the database and start again. You can do that with the command:

        python manage.py shop flush

Otherwise each customer created is also a user with a default password set in the management/commands/populate_tables.py file. 


To run all the necessary commands above in a single file for the codio/linux environment, we can run the `build.sh` file as follows:
        
        chmod +x build.sh
        ./build.sh

You can launch django with the usual command:

        python manage.py runserver

With the server running, you can navigate around both parts of the application:
1. Go around the general website and notice what's working, what's bare-bones, and other issues. This is not finished, but a work in progress to illustrate how you might build a shopping application. 
2. Go to localhost:8000/admin and login with your superuser credentials. There you'll see the Django admin interface. From here you can also add products, and customers. The models listed here are specified in the shop/admin.py file.
