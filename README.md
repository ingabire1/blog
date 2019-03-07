Blog App

 Developed by Ingabire Aimee Sylvie on March 6st, 2019

Description
A web application where one can start blogs and users can comment on the topic or start a blog of their own. user can view blogs click on article and view the whole blog post. and it display the whole blogs. user can write comments on the comment test area box.the name also is required.then the comment is displayed on the blog content. you fill subscription form that user can receive a subscription confirmation email. we can also writte and  add blog, delete and update blogs and delete comments

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

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
