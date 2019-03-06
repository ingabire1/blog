Blog App

 Developed by Ingabire Aimee Sylvie on March 6st, 2019

Description
Blog is a web application where user can post the quote and see the blogs.and can subscribes to get the latest updates on post. Users can subscribe to the blog to get the latest updates on articles.The blog supports comments from readers and blog writers can determine whether to delete the comments or not. Users can also delete blog posts at their discretion.After the writer has posted a new blog post, subscribers will receive an email notification with a link to the blog post.

Specifications
user can view blogs click on article and view the whole blog post. and it display the whole blogs. user can write comments on the comment test area box.the name also is required.then the comment is displayed on the blog content. you fill subscription form that user can receive a subscription confirmation email.

writer can add blog, delete and update blogs and delete comments

Set-up and Installation
Prerequiites

Python 3.6
Ubuntu software
Clone the Repo
Run the following command on the terminal: git clone : && cd ipblogs

Create a Virtual Environment
Run the following commands in the same terminal:

sudo apt-get install python3.6-venv python3.6 -m venv virtual source virtual/bin/activate curl https://bootstrap.pypa.io/get-pip.py | python pip install flask

Prepare environment variables
export DATABASE_URL='postgresql+psycopg2://:@localhost/blog'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://:@localhost/blog_test'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=
export MAIL_PASSWORD=
Run Database Migrations
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
Running the app in development
In the same terminal type: python3 manage.py server

Open the browser on http://localhost:5000/

Known bugs
no bugs yet displayed on the project

Technologies used
Python 3.6
HTML
Bootstrap 4
Heroku
Postgresql
Support and contact details
Contact me on ingabire.sylvie@gmail.com for any support want.

License
MIT Copyright (c) 2019 Ingabire Aimee Sylvie