from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import numpy as np
import util as utils
import data_preparation as data_preparation
import preprocessing as preprocessing

konfig = utils.load_params(str(utils.dir_parent()) + utils.get_params())
model_data = utils.pickle_load(str(utils.dir_parent()) + utils.cek_path_os(konfig["production_model_path"]))

class api_data(BaseModel):
    HARGA : int
    LB : int
    LT : int
    KT : int
    KM : int
    GRS : int

app = FastAPI()

@app.get("/")
def home():
    return "Hello, FastAPI up!"

@app.post("/predict/")
def predict(data: api_data):    
    # Convert data api to dataframe
    data = pd.DataFrame(data).set_index(0).T.reset_index(drop = True)  # type: ignore
    data.columns = konfig["predictors"]

    # Convert dtype
    data = pd.concat(
        [
            data[konfig["predictors"][:]].astype(np.int64)  # type: ignore
        ],
        axis = 1
    )

    # Check range data
    try:
        data_preparation.check_data(data, config, True)  # type: ignore
    except AssertionError as ae:
        return {"res": [], "error_msg": str(ae)}

    # Predict data
    y_pred = model_data.predict(data)

    if y_pred[0] == 0:
        y_pred = "Tidak ada api."
    else:
        y_pred = "Ada api."
    return {"res" : y_pred, "error_msg": ""}

if __name__ == "__main__":
    uvicorn.run("api:app", host = "0.0.0.0", port = 8080)
