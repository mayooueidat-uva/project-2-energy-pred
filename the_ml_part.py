import logging
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import train_test_split
import pymongo
from pymongo import MongoClient, errors
import glob 
import json
from sklearn.model_selection import GridSearchCV 
from sklearn.model_selection import KFold
from sklearn.ensemble import HistGradientBoostingRegressor
import matplotlib.pyplot as plt
import shap

# initialising mongo database 
client = MongoClient("mongodb+srv://<username>:<password>@ds4320proj2.p0udp7x.mongodb.net/")
# print(client.list_database_names())

# loading up all our data to use
ml_data = pd.DataFrame(list(database.data_for_ml.find({})))

# taking a look at all of our data 
# ml_data.info()

# feature matrix 
X_unprocessed = ml_data.iloc[:, 4:44]
# X_unprocessed.head()

# target vector 
y_unprocessed = ml_data.iloc[:, 46]
# y_unprocessed.head()

# im going to do a magic trick 
Xy = pd.concat([X_unprocessed, y_unprocessed], axis=1) 
# Xy.head()

# interpolate data 
# to get rid of NaNs
Xy_int = Xy.interpolate()
# Xy_int.head()

# interpolated dataframe 
Xy_int = Xy_int.dropna()
# Xy_int.info()

# final feature matrix and target vector 
X = Xy_int.iloc[:, 0:39]
y = Xy_int.iloc[:, -1]

# print(X.head())
# print(y.head())

# train-test-split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# model selection part 
cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

hist_model = HistGradientBoostingRegressor(max_iter=2500, random_state=42)

hist_model.fit(X_train, y_train)

max_depth_values = [5, 10, 15]

hist_param_grid = {
    'max_depth': max_depth_values,
    'learning_rate': [0.01, 0.1, 0.3]
}

hist_grid = GridSearchCV(hist_model, hist_param_grid, cv=cv,
                       scoring='neg_root_mean_squared_error', n_jobs=-1, verbose=1)

hist_grid.fit(X_train, y_train)

# best parameters 
# print("Best parameters:", hist_grid.best_params_)
# print("Best CV score:", hist_grid.best_score_)

best_model = hist_grid.best_estimator_

# test score 
test_score = best_model.score(X_test, y_test)
# print("neg root mean squared error:", test_score)

# calculating y_pred
y_pred = hist_grid.best_estimator_.predict(X_test)

# viewing the most important features predicting excess readm 
explainer = shap.Explainer(best_model)
shap_values = explainer(X_test)

shap.plots.bar(shap_values)
plt.title("Most important features for predicting readm") 