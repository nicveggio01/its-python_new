

from flask import Flask

app = Flask(__name__)

@app.route("/")
def descrizione()-> str:
    return "Questo è il primo esercizio di flask"