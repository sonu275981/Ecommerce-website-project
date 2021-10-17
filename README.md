Django E-commerce


This is a very simple e-commerce website built with Django.

1-Project Summary

The website displays products. Users can add and remove products to/from their cart while also specifying the quantity of each item. They can then enter their address and choose Stripe to handle the payment processing.

2-Running this project


3-To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

pip install virtualenv


4-Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

virtualenv env


5-That will create a new folder env in your project directory. Next activate it with this command on mac/linux:

source env/bin/active


6-Then install the project dependencies with

pip install -r requirements.txt


7-Now you can run the project with this command

python manage.py runserver


8-Note if you want payments to work you will need to enter your own Stripe API keys into the .env file in the settings files.

