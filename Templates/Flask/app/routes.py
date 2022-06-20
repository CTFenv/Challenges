#!/usr/bin/python

# Import statements
import os
import sqlite3
from flask import render_template, make_response
from app import app
from dotenv import load_dotenv  # Centralized credentials library


# Load db and dotenv
BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASEDIR, 'database.db')
load_dotenv(os.path.join(BASEDIR, '.env'))


# General functions (database connection, flags and more)


# App routes
@app.route('/', methods=['GET'])
def index():
    vars = {
        "title": "Homepage",
        "page": "home",
    }
    return render_template('home.html', vars=vars)
