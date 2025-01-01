import os
from flask import Flask, render_template
from views import views

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return """<h1>This is profile</h1>"""

#app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT",8080)))