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

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

Base = automap_base()
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
    prev_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= prev_yr).all()

    prcp_results = []
    for date, prcp in results:
        results_dict = {}
        results_dict[date] = prcp
        prcp_results.append(results_dict)

# Return the JSON representation of your dictionary.
    return jsonify(prcp_results) 

@app.route("/api/v1.0/stations")
def stations():
# Return a JSON list of stations
    query_act_stations = session.query(measurement.station, func.count(measurement.station)).\
                    group_by(measurement.station).\
                    order_by(func.count(measurement.station).desc()).all()
    station_list = list(np.ravel(query_act_stations))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
# Query the dates and temperature observations of the most-active station for the previous year of data.
    prev_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= prev_yr).all()
    query_act_stations = session.query(measurement.station, func.count(measurement.station)).\
    prev_yr_temps = session.query(measurement.tobs).filter(
    measurement.date >= prev_yr,
    measurement.station == 'USC00519281'
    ).all()
    
    tobs_results = []
    for date, tobs in results:
        tobs_results_dict = {}
        tobs_results_dict[date] = tobs
        tobs_results_dict.append(tobs_results_dict)

    return jsonify(tobs_results)

# Return a JSON list of temperature observations for the previous year.

#@app.route("/api/v1.0/<start>")
#def start(start):
# Return a JSON list of min, avg, max of temperature from a start date
    #date = dt.datetime.strptime(start, "%y-%m-%d").date()

#@app.route("/api/v1.0/<start>/<end>")
#def start_end(start, end):
# Return a JSON list of min, avg, max of temperature from a start date and end date




if __name__ == '__main__':
    app.run(debug=True)