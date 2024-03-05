#Imports 
import requests
from flask import Flask, render_template, request



app = Flask(__name__) 

#Calgary Building Permit API Info
CGY_GAPI = "https://data.calgary.ca/resource/c2es-76ed.geojson"
parameters = "&$select=issueddate,workclassgroup,contractorname,communityname,originaladdress, LocationsGeoJSON " 


@app.route("/", methods = ["get", "post"])
def main(): 
    return render_template("main.html") 