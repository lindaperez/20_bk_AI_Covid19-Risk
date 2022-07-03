# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
import joblib
import pickle
#import requests
import json


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','') or "sqlite:///db.sqlite"
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://','postgresql://') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

result = create_classes(db)
Patient = result['Patient']

# create route that renders index.html template
@app.route("/")
def home():
    #return render_template("index.html")
    return redirect("/list", code=302)


# Query the database and register the jsonified results
@app.route("/register", methods=["GET", "POST"])
def register():
    params = {}
    if request.method == "POST":
        if 'patientFirstName' in request.form and request.form['patientFirstName'].strip()!='':
            params['first_name'] = request.form["patientFirstName"]
        if 'patientLastName' in request.form and request.form['patientLastName'].strip()!='':
            params['last_name'] = request.form["patientLastName"]
        if 'patientAge' in request.form and request.form['patientAge'].strip()!='':
            params['newage'] = int(request.form["patientAge"])
        params['intubated'] = int("patientIntubated" in request.form.keys())
        params['diabetes'] = int('patientDiabetes' in request.form.keys())
        params['asthma'] = int('patientAsthma' in request.form.keys())

        params['immunosup'] = int('patientImmunosup' in request.form.keys())
        params['hypertension'] = int('patientHypertension' in request.form.keys())
        params['cardiovascular'] = int('patientCardiovascular' in request.form.keys())
        params['obesity'] = int('patientObesity' in request.form.keys())
        params['renal_chronic'] = int('patientRenalChronic' in request.form.keys())
        params['tobacco'] = int('patientTobacco' in request.form.keys())

        params['closed_contanct'] = int('patientClosedContanct' in request.form.keys())
        params['icu'] = int('patientICU' in request.form.keys())

        pat = Patient(**params)
        db.session.add(pat)
        db.session.commit()
        return redirect("/list", code=302)

    return render_template("form.html")

@app.route("/list", methods=["GET", "POST"])
def list():
    if request.method == "GET":
        patients = Patient.query.all()
        for pat in patients:
            print(pat.first_name)
        return render_template("index.html", patients=patients)

    return render_template("form.html")

@app.route("/listPatients")
def listPatients():
    if request.method == "GET":
        patients = Patient.query.all()
        for pat in patients:
            print(pat.first_name)
        return render_template("listPatients.html", patients=patients)

    return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
def predict():

    filename = 'ee_model_icu_v2.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))
    from numpy import genfromtxt
    X_test_scaled = genfromtxt('X_test_scaled.csv', delimiter=',')
    y_pred_eec = loaded_model.predict(X_test_scaled)
    predicted = json.dumps(y_pred_eec.tolist())

    return jsonify({'prediction':predicted})


# @app.route("/api/pals")
# def pals():
#     results = db.session.query(Patient.name).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]

#     pet_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",
#         "lat": lat,
#         "lon": lon,
#         "text": hover_text,
#         "hoverinfo": "text",
#         "marker": {
#             "size": 50,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

#     return jsonify(pet_data)


if __name__ == "__main__":
    app.run()

