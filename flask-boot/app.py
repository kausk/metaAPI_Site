# import the Flask class from the flask module
from flask import Flask, render_template, request, redirect, url_for
import requests
import simplejson as json
from urllib2 import Request, urlopen
from pymongolab import MongoClient
import sys
import pymongo

##initializing the mongoclient
MONGODB_URI = "mongodb://meta:meta@dbh76.mongolab.com:27767/armeta" 
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()



# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return redirect(url_for('feed'))  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/testdb')
def test_db():
	db = con["armeta"]
	column = db.test_collection

	post = column.insert({"title": "My new post"})
	return post

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

@app.route('/addtext', methods=['GET', 'POST'])
def add_text():
    error = None
    if request.method == 'POST':
    	'''
        if request.form['number'] != 'admin' or request.form['text'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        '''
        ###data which will be submitted to the meta
        Data = [
        {
        	'number' : request.form['number'],
        	'text' : request.form['text']

        }

     	]
        comments = db['comments']
        comments.insert(Data)

        ##return to feed
        return render_template('feed.html')


    return render_template('addtext.html')

@app.route('/feed')
def feed():
	return render_template('feed.html')

@app.route('/addpic', methods=['GET', 'POST'])
def add_pic():
    error = None
    if request.method == 'POST':
    	'''
        if request.form['number'] != 'admin' or request.form['text'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        '''
        ###data which will be submitted to the meta
        Data = [
        {
        	'number' : request.form['number'],
        	'pic' : request.form['pic']

        }

     	]
        pics = db['pics']
        pics.insert(Data)

        ##return to feed
        return render_template('feed.html')
    return render_template('addpic.html')

@app.route('/one', methods=['GET', 'POST'])
def one():
	return render_template('one.html')



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

