from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('homepage.html')
  
@app.route('/events', methods=["POST", "GET"])
def login():
  return render_template("events.html")

@app.route('/RAs', methods=["POST", "GET"])
def get_username():
  return render_template("RAs.html")
  


app.run(host='0.0.0.0', port=81)
