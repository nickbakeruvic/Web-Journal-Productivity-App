from flask import Flask, render_template, request
import os
import base64
import json


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
  #initDetection()
  app.run()