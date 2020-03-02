from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def default():
    return render_template('default.html')

