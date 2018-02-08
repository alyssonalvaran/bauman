from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
	try:
		return render_template('home.html')
	except TemplateNotFound:
		abort(404)

@app.route("/signup")
def signup():
	try:
		return render_template('signup.html')
	except TemplateNotFound:
		abort(404)

@app.route("/login")
def login():
	try:
		return render_template('login.html')
	except TemplateNotFound:
		abort(404)

@app.route("/cart")
def cart():
	try:
		return render_template('cart.html')
	except TemplateNotFound:
		abort(404)