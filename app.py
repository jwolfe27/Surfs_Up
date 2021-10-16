import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
# Set up our database engine
engine = create_engine("sqlite:///hawaii.sqlite")
#Function allows us to access and query our SQLite database file
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)
#Assign variables to each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station
#Create session link from Python to our database
session = Session(engine)
# Define our Flask App
app = Flask(__name__)
# Define the welcome route
@app.route("/")
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')
        
    