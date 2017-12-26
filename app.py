
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
def home_page():
	return render_template("index.html")



if __name__ == '__main__':
	app.run()
