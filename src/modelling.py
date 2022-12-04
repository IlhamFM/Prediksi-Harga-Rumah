import util as utils
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
import math

def load_train_clean(params: dict):
    # Load train set
    X_train = utils.pickle_load(str(utils.dir_parent()) + utils.cek_path_os(params["train_clean_set_path"][0]))
    y_train = utils.pickle_load(str(utils.dir_parent()) + utils.cek_path_os(params["train_clean_set_path"][1]))

    return X_train, y_train

def load_test(params: dict):
    # Load tets set
    X_test = utils.pickle_load(str(utils.dir_parent()) + utils.cek_path_os(params["test_set_path"][0]))
    y_test = utils.pickle_load(str(utils.dir_parent()) + utils.cek_path_os(params["test_set_path"][1]))

    return X_test, y_test
    
def get_baseline_pred():
    return y_train.mean()
    
def get_baseline_rsme():
    baseline_mse = mean_squared_error(y_train, np.ones(len(y_train)) * np.float64(get_baseline_pred()))
    #print(get_baseline_pred())
    #print(math.sqrt(baseline_mse))
    return math.sqrt(baseline_mse)
    
def get_scores_rsme(lr):
    scores_rsme = cross_val_score(estimator = lr,
                         X = X_train,
                         y = y_train,
                         cv = 5,
                         scoring = "neg_root_mean_squared_error")
    return scores_rsme
    
def train_model(X_train, y_train, X_test, y_test):
    lr = LinearRegression()
    scores = get_scores_rsme(lr)
    lr_cv_scores = - np.mean(get_scores_rsme(lr))
    
    
    lr.fit(X = X_train, y = y_train)
    
    y_pred = lr.predict(X_train)
    
    prediction_train = math.sqrt(mean_squared_error(y_pred, y_train))
    print("prediction_train", prediction_train)
    baseline_mse = get_baseline_pred()
    
    comparison_rmse = 100*(get_baseline_rsme() - prediction_train) / get_baseline_rsme()
    print(f"RMSE turun {comparison_rmse:.2f} %")
    
    print(lr.coef_)
    
    y_test_pred = lr.predict(X_test)
    
    prediction_test = math.sqrt(mean_squared_error(y_test_pred, y_test))
    print(prediction_test)
    
    comparison_rmse_test = 100*(get_baseline_rsme() - prediction_test) / get_baseline_rsme()
    print(f"RMSE turun {comparison_rmse_test:.2f} %")
    
    return lr
    
    
if __name__ == "__main__":
    
    konfig = utils.load_params(str(utils.dir_parent()) + utils.get_params())
    
    X_train, y_train = load_train_clean(konfig)
    X_test, y_test = load_test(konfig)
    
    lr = train_model(X_train, y_train, X_test, y_test)
    
    utils.pickle_dump(lr, str(utils.dir_parent()) + utils.cek_path_os(konfig["production_model_path"]))
    
    
    
    
    
    