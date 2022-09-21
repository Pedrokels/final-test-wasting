import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pickle
import pandas as pd
import sklearn

app = FastAPI()

classifier = pickle.load(open("model_pickel.pkl", "rb"))

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.get('/{name}')
def get_name(name : str):
    return {'message': f'Hello, {name}'}
    
@app.post("/predict")
def predict_banknote(data:BankNote):
    data = data.dict()
    age_child = data['age_child']
    sex_child = data['sex_child']
    bw_grams = data['bw_grams']
    feeding = data['feeding']
    ethnicity = data['ethnicity']
    agegroup_mom =data['agegroup_mom']
    csc_mom = data['csc_mom']
    psc1 = data['psc1']
    educ_mom = data['educ_mom']
    educ1_hh = data['educ1_hh']
    psoc_hh = data['psoc_hh'] 
    urbanity = data['urbanity'] 
    wcooking = data['wcooking']
    
    print(classifier.predict([[age_child,sex_child,bw_grams,feeding,ethnicity,agegroup_mom,csc_mom,psc1,educ_mom,educ1_hh,psoc_hh,urbanity,wcooking]]))
    prediction = classifier.predict([[age_child,sex_child,bw_grams,feeding,ethnicity,agegroup_mom,csc_mom,psc1,educ_mom,educ1_hh,psoc_hh,urbanity,wcooking]])

    
    if prediction == 0: 
        prediction =  ('Childs wasting is Normal')
    else:
        prediction = ('Childs wasting is Wasting')
    
    return{
        'prediction' : prediction
    }
    
if __name__ == '__main__':
    uvicorn.run(app, debug=True)