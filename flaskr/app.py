import os
from flask import Flask, render_template
from views import views
from db import insertQuery
import uuid

app = Flask(__name__)

def generateUUID():
    return str(uuid.uuid4())
uuid1=generateUUID()
insertQuery(uuid1, "Selvan", "Ritesh", "Bangalore","Male", "9876543210")
@app.route('/locate')
def homepage():
    return render_template('index.html')

@app.route('/admin')
def profile():
    return """<h1>This is profile</h1>"""

#app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT",8080)))