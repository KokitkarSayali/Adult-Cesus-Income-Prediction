import numpy as np
import pandas as pd
import pickle
from flask import Flask,jsonify,request,render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    if request.method == 'POST':
        
        age_value = request.form['age']
        edu_num_value = request.form['education-num']
        marital_value = request.form['marital-status']
        occupation_value = request.form['occupation']
        relationship_value = request.form['relationship']
        gain_value = request.form['capital-gain']
        hours_value = request.form['hours-per-week']
        

    
        features = [age_value, edu_num_value,marital_value, occupation_value, relationship_value,gain_value,hours_value]
        
        int_features = [int(x) for x in features]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        
        if prediction == 1:
            output = "Income is more than 50K"
        elif prediction == 0:
            output = "Income is less than 50K"
        
    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True,port=5000)