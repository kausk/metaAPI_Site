# import the Flask class from the flask module
from flask import Flask, render_template
import requests
import simplejson as json
from urllib2 import Request, urlopen

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/apiget')
def get_data():
	request = Request('http://private-59c72-metapi.apiary-mock.com/notes') ##get content from apiary
	response_body = urlopen(request).read()
	return response_body



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

