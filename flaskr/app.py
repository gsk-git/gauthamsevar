import os
import uuid
from flask import Flask, render_template, request as req, redirect, url_for
from views import views
import db


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return "Voila  you got it!"

@app.route('/submit', methods=['POST'])
def fetchData():
    email = req.form['email-id']
    fname = req.form['firstName']
    lname = req.form['lastName']
    mobile = req.form['mobile']
    city = req.form['city']
    gen = req.form['gender']
    pswd = req.form['password']
    id = str(uuid.uuid4())
    formData = {
        "lname": lname,
        "fname": fname,
        "email": email,
        "city": city,
        "gen": gen,
        "mobile": mobile,
        "pswd": pswd,
        "uuid": id
    }
    db.insertQuery(id, lname, fname, email, city, gen, mobile, pswd)
    return redirect('/')

@app.route('/admin')
def profile():
    return """<h1>This is profile</h1>"""

#app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT",8080)))