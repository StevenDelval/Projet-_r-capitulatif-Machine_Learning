import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
pickle_in = open('model.pkl', 'rb') 
model_XGBoost = pickle.load(pickle_in)

cols = model_XGBoost[:-1].get_feature_names_out()
new_columns = [w.replace('pipeline-1__', '') for w in cols]
genre_columns = [w  for w in new_columns if "genre" in w]

app = FastAPI()

class Request(BaseModel):
   duration_ms: int
   explicit: int
   track_number: int
   danceability: int
   energy: int
   key: int
   loudness: int
   mode: int
   speechiness: int
   acousticness: int
   instrumentalness: int
   liveness: int
   valence: int
   tempo: int
   time_signature: int
   genre: str

@app.get("/")
async def root():
    return {"Hello_World":"Bonjour_Monde"}


@app.post("/predict/")
async def predict(data:Request):
    

    pred = pd.DataFrame(data.dict(),index=[0])
    pred = pd.get_dummies(pred, columns=['genre'], sparse=False, prefix=None)
    for col in genre_columns:
        if not(col in  pred.columns):
            pred[col]=0
    
    pop_pred = model_XGBoost.predict(pred)
    
    return {'pop':str(pop_pred[0])}