
from flask import Flask,request
import joblib
model=joblib.load(r'linear-model.pkl')
app=Flask(__name__)
@app.route('/',methods=['POST'])

def abcd():
    data=request.get_json(force=True)
    data=data['test']
    out=model.predict(data)
    return str(out)

