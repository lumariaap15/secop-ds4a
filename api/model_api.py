import pandas as pd
import uvicorn
import nest_asyncio
nest_asyncio.apply()
from fastapi import FastAPI
import joblib
import warnings
warnings.filterwarnings("ignore")

def prepare_model_data(x_variables):
    return x_variables

def load_model():
    model = open('model.pkl', 'rb')
    return joblib.load(model)

port = '8051'
api_url = 'http://0.0.0.0:' + port + '/'

fastapi_model = FastAPI(root_path='')

@fastapi_model.post('/predict/')
async def XGBoost_predict(x_variables):

    prepared_data = prepare_model_data(x_variables)
    #prediction = load_model().predict(prepared_data)
    return {'Delay prediction': 'No'}

print(f'API Swagger URL: {api_url}docs')
uvicorn.run(fastapi_model, port=port, host='0.0.0.0')