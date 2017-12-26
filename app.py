
from flask import Flask, render_template
import datetime
import pytz # timezone 
import requests
import os

app = Flask(__name__)

@app.route('/profile/<name>')
def home_page(name):
	return render_template("profile.html", name=name)



if __name__ == '__main__':
	app.run()
