import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import filedialog
from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os

app = Flask(_name_)

@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/new_customer')
def new_customer_page():
	return render_template('new_customer.html')




app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
	app.run(debug=False)
