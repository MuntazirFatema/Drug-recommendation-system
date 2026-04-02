from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('drug_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        bp = int(request.form['bp'])
        cholesterol = int(request.form['cholesterol'])
        na_to_k = float(request.form['na_to_k'])

        prediction = model.predict([[age, sex, bp, cholesterol, na_to_k]])[0]
        drug_mapping = {0:'DrugA', 1:'DrugB', 2:'DrugC', 3:'DrugX', 4:'DrugY'}
        result = drug_mapping[prediction]
        
        return render_template('index.html', result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
    
