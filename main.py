from flask import Flask, request
import pandas as pd

df = pd.read_csv('./data/provider012622.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MN Provider details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/provider/<value>', methods=["GET"])
def provider_type(value):
    print('value: ', value)
    filtered = df[df['PROVIDER_TYPE_CD'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.route('/provider/<value>/sex/<value2>', methods=["GET"])
def icdcode2(value, value2):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")

if __name__=='__main__':
    app.run(debug=True)