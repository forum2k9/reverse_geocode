import pandas as pd
from datetime import datetime
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
	csv_file = request.files['data_file'] # read csv from form html field

# ============ USE PANDAS READ CSV FILE ================
	df = pd.read_csv(csv_file)
	col_long = list(df['Longitude'])
	col_lat = list(df['Latitude'])

# ============ R.GEOCODE AND ADD TO LIST ================
	# nom = ArcGIS()
	# nom = GoogleV3(api_key="AIzaSyDhmLVNREF7BUcX7UQ87euCR-yz0h3frXE")
	# nom = Nominatim()

# Try geocode with Google API, if it fails, 
# then try with Nominatim API, if that also failed, return None

	add_list = []

	for lat, lon in zip(col_lat, col_long):
		try:
			try: # Google API
				nom = GoogleV3(api_key="AIzaSyDhmLVNREF7BUcX7UQ87euCR-yz0h3frXE")
				n = nom.reverse((lat, lon), timeout=10) # Lat, Long

				data = (lat, lon, n[0])
				add_list.append(data)
		        
			except Exception: # OpenStreetMap API
				nom = Nominatim()
				n = nom.reverse((lat, lon), timeout=10) # Lat, Long

				data = (lat, lon, n[0])
				add_list.append(data)

		except Exception:
			data = (lat, lon, "None")
			add_list.append(data)


# =================================
	# for lat, lon in zip(col_lat, col_long):

	# 	n = nom.reverse((lat, lon), timeout=10) # Lat, Long

	# 	data = (lat, lon, n[0])
	# 	add_list.append(data)



# ============= SAVE ===============
	now_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
	add_list_df = pd.DataFrame(add_list, columns=['Latitude', 'Longitude', 'Address'])
	file_name = r'static/results/rGeocode_Result'+ now_date +'.csv'
	add_list_df.to_csv(file_name, index=None)
	
	return render_template("r_geocoder.html", add_list=add_list_df, file_name=file_name)




if __name__ == '__main__':
	app.run(debug=True)
