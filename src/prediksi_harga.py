import pandas as pd
import numpy as np
import util as utils
import pickle

lb = input("Masukkan luas bangunan (m2) : ")
lt = input("Masukkan luas tanah (m2) : ")
kt = input("Masukkan jumlah kamar tidur : ")
km = input("Masukkan jumlah kamar mandi : ")
grs = input("Masukkan kapasitas garasi : ")

dict_x = {
    "LB" :[lb],
    "LT" : [lt],
    "KT" : [kt],
    "KM" : [km],
    "GRS" : [grs]
}

konfig = utils.load_params(str(utils.dir_parent()) + utils.get_params())
file = str(utils.dir_parent()) + utils.cek_path_os(konfig["production_model_path"])
loaded_model = utils.pickle_load(file)
model_data = utils.pickle_load(str(utils.dir_parent()) + utils.cek_path_os(konfig["production_model_path"]))
df = pd.DataFrame(dict_x)
y_pred = loaded_model.predict(df)
print("==================================================")
print("Kisaran harga rumah di tebet sebesar", int((y_pred)))
print("==================================================")