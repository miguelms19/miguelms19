
from flask import Flask, render_template
import datetime
import pytz # timezone 
import requests
import os

app = Flask(__name__)

@app.route('/profile/<name>')
def profile_page(name):
	return render_template("profile.html", name=name)

@app.route('/')
@app.route('/<user>')
def home_page(user=None):
	return render_template("index.html", user=user)



if __name__ == '__main__':
	app.run()
