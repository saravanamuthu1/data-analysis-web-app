from distutils.debug import DEBUG
from distutils.log import debug
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import pandas as pd
from application import Application

ALLOWED_EXTENSIONS = {'csv'}
obj1=Application()
app= Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    shape_data=""
    val = []
    if request.method == "POST" and 'csv_data' in request.files:
        file = request.files['csv_data']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/storage',filename))
        df=pd.read_csv(os.path.join('static/storage',filename))
        shape_data=obj1.load_data(df)
        val=df.columns
    return render_template('upload.html',shape_data=shape_data,val=val)

@app.route('/describe',methods=['GET','POST'])
def describe():
    describe_value=None
    describe_value=obj1.describe_data()
    return render_template('describe.html',describe_value=describe_value.to_html())

@app.route('/clean',methods=['GET','POST'])
def clean():
    clean_value=""
    if request.method == "POST":
        clean_value=obj1.clean_data()
    return render_template('clean.html',clean_value=clean_value)
