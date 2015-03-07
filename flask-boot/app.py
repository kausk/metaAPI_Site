# import the Flask class from the flask module
from flask import Flask, render_template, request, redirect, url_for
import requests
import simplejson as json
from urllib2 import Request, urlopen
from pymongolab import MongoClient

##initializing the mongoclient
MongoClient('K4o23oEbq20nb1tS-1kmkAqGuTmE8aed')

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/testdb')

@app.route('/apiget')
def get_data():

	request = Request('http://private-59c72-metapi.apiary-mock.com/notes') ##get content from apiary
	response_body = urlopen(request).read().info()
	return response_body

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


    'https://api.mongolab.com/api/1/databases?apiKey=K4o23oEbq20nb1tS-1kmkAqGuTmE8aed'
    ##mongolab url
@app.route('/apipost')
def post_data():

	values = """
	  {
	    "title": "Buy cereal and bread for lunch."
	  }
	"""

	headers = {
	  'Content-Type': 'application/json'
	}
	request = Request('http://private-59c72-metapi.apiary-mock.com/notes', data=values, headers=headers)

	response_body = urlopen(request).read()
	return response_body


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

