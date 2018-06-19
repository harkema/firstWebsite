from flask import Flask, render_template
from dbconnect import connection

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("base.html", title='Welcome')


@app.route('/home')
def home():
    user = {'username': 'Alice'}
    return render_template("homepage.html", user=user)
if __name__ == "__main__":
    app.run(debug=True)