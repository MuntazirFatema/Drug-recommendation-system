from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('drug_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age=request.form['age'],
        sex=request.form['Sex'],
        bp=request.form['bp'],
        cholestrol= request.form['cholestrol'],
        na_to_k=request.form['na_to_k' ]

        prediction=model.predict([[age,sex,bp,cholestrol,na_to_k]])
        drug_mapping={0:'DrugA' ,1:'DrugB' ,2:'DrugC' ,3:'DrugX' ,4:'DrugY'}
        result=drug_mapping[prediction]
        return render_template('index.html' ,result)
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    