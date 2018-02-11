from flask import Flask, render_template, request

app = Flask(__name__)


@app.route( '/')
def index():
	return render_template("index.html")


@app.route('/index_2')
def index_2():
	url_name = 'https://www.w3schools.com/'
	return render_template("index_2.html", url_name=url_name)



if __name__ == '__main__':
	app.run(debug=True)
