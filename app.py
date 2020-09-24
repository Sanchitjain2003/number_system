from flask import Flask, render_template, redirect, url_for, request, flash
import requests, yaml
#from flask_mysqldb import MySQL
import joblib
db = yaml.load(open('db.yaml'))


import json

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        details = request.form
        
    return render_template('result.html', details=details)
@app.route('/aboutus', methods=["GET","POST"])
def aboutus():
	return render_template('aboutus.html')

if __name__ == '__main__':
   app.run(debug = True)
