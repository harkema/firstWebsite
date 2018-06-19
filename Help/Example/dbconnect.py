Example/exampledb.db                                                                                0000644 0001750 0001750 00000000000 13304064507 014215  0                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               Example/run.py                                                                                      0000644 0001750 0001750 00000000577 13305265100 013137  0                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               from flask import Flask, render_template
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
    app.run(debug=True)                                                                                                                                 Example/static/                                                                                     0000755 0001750 0001750 00000000000 13302065277 013251  5                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               Example/static/styles/                                                                              0000755 0001750 0001750 00000000000 13302076036 014567  5                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               Example/static/styles/base.css                                                                      0000644 0001750 0001750 00000001474 13302076036 016221  0                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               body {
    padding: 30px;
    margin: 10px;
    border: 5px solid #f1eff9;
    width: 350px;
    height: 350px;
}

h1 {
    padding: 20px;
    font-family: "Courier New", monospace;
    background-color: #f1eff9;
    width: 300px;
    height: 75px;
    text-align: center;

}

p {
    border: 5px inset #635b99;
    color: #3d3768;
    width:300px;
    height:100px;
    background-color: #f1eff9;
    padding: 20px;
    font-family: "Courier New", monospace;

}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

li {
    float: left
}

li a{
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active){
    background-color: #111;
}


li a.active{
    background-color: #635b99;
}                                                                                                                                                                                                    Example/templates/                                                                                  0000755 0001750 0001750 00000000000 13303602236 013751  5                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               Example/templates/homepage.html                                                                     0000644 0001750 0001750 00000000210 13303601150 016407  0                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               {% extends "base.html" %}

{% block body %}
    <h1> Wow it’s a new page </h1>

    <p>Hello, {{ user.username }} </p>

{% endblock %}                                                                                                                                                                                                                                                                                                                                                                                        Example/templates/base.html                                                                         0000644 0001750 0001750 00000001174 13303602236 015554  0                                                                                                    ustar   emmi6426                        emmi6426                                                                                                                                                                                                               <!DOCTYPE html>
<html>
    <head>
        <link rel= "stylesheet" type= "text/css" href= "{{url_for('static',filename='../static/styles/base.css') }}" >
        {% if title %}
        <title> {{ title }}- Your Site </title>
        {% else %}
        <title>Welcome to Site</title>
        {% endif %}
    </head>

    <body>

    <ul>
        <li><a href="/index">Index</a></li>
        <li><a href="/home">Page 2</a></li>
        <li><a href="/page">Page 3</a></li>
    </ul>
    <hr>

        {% block body %}

            <h1>Hello World</h1>

            <p>This is part of the body.</p>

        {% endblock%}
    </body>
</html>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    