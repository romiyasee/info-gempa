from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/klaster')
def klaster():
    df = pd.read_csv('static/remark_per_cluster_columns.csv')
    df.columns = ['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3']
    table_data = df.to_dict(orient='records')
    return render_template('klaster.html', table_data=table_data)

@app.route('/peta')
def peta():
    return render_template('peta.html')

if __name__ == '__main__':
    app.run(debug=True)
