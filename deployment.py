import json
import numpy as np
import pickle
import sklearn
from flask import Flask,request,render_template
locations =None
data_columns=None
model=None
app=Flask(__name__)
with open('columns.json','r') as f:
        data_columns=json.load(f)['data_columns']
        locations=data_columns[3:]

with open('rf_model_final.pickle','rb') as f:
    model=pickle.load(f)

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
        
    
    return round(model.predict([x])[0],2)

@app.route('/')
def homepage():
     return render_template('values.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
     if request.method=='POST':
          loc=request.form['location']
          sqft=float(request.form['area'])
          bhk=float(request.form['bhk'])
          bath=float(request.form['bath'])
          pred=get_estimated_price(loc,sqft,bhk,bath)
          return render_template('values.html',output='Price :{}'.format(pred))
          
        #   return loc,sqft,bhk,bath

if __name__=='__main__':
     app.run(debug=True)

# res=get_estimated_price('1st phase jp nagar',1000,2,2)
# print(res)


