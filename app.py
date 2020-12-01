from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    df = pd.read_csv("data.csv", index_col=0, header=None)
    return df.to_string()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')