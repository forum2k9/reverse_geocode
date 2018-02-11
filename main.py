import pandas as pd
from geopy.geocoders import Nominatim, ArcGIS, GoogleV3
from flask import Flask, render_template, request
# import requests

written_by = "www.UmarYusuf.com"


app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")




@app.route("/r_geocoder", methods=['GET', 'POST'])
def r_geocoder():
	try:
		my_lat = float(request.form['mylat'])
		my_long = float(request.form['mylong'])
	except Exception:
		my_lat = None
		my_long = None

	nom = ArcGIS()

	if (my_lat or my_long) == None:
		address = "Invalid Lat/Long values"
		return render_template("r_geocoder.html", my_lat=my_lat, my_long=my_long, address=address)
	else:
		try:
			# n = nom.reverse((32.839097, -96.663127), timeout=10) # Lat, Long
			n = nom.reverse((my_lat, my_long), timeout=10) # Lat, Long
			address = n.address
			return render_template("r_geocoder.html", my_lat=my_lat, my_long=my_long, address=address)
		except Exception:
			return render_template("r_geocoder.html", my_lat=my_lat, my_long=my_long, address="No Address for the provided Lat/Long values!")

if __name__ == '__main__':
	app.run(debug=True)
