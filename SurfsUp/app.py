# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
data = Base.classes.data

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
# Converting last 12 months of precipitation data to dictionary

# Return the JSON representation of your dictionary.
     
@app.route("/api/v1.0/stations")
def stations():
# Return a JSON list of stations
    
@app.route("/api/v1.0/tobs")
def tobs():
# Query the dates and temperature observations of the most-active station for the previous year of data.

# Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/<start>")
def start(start):
# Return a JSON list of min, avg, max of temperature from a start date
    
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
# Return a JSON list of min, avg, max of temperature from a start date and end date