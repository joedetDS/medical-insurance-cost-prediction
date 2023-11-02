# Medical Insurance Cost Prediction System

A machine learning project that predicts medical insurance costs based on various factors such as age, gender, BMI, smoking status, and region.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Conclusion](#conclusion)


## Overview

The "Medical Insurance Cost Prediction System" is a machine learning application designed to predict medical insurance costs for health related companies particularly health maintenance organizations in NIgeria. It utilizes a dataset containing information about policyholders, including their age, gender, BMI, smoking status, and region, to build a predictive model. The objective is to assist insurance providers in estimating insurance costs more accurately.

## Dataset

The dataset used for this project is sourced from https://www.kaggle.com/datasets/mirichoi0218/insurance. It contains 1338 samples and 7 features, which are:
- Age
- Gender
- BMI (Body Mass Index)
- Smoking Status
- Region
- Medical Insurance Cost (target variable)

The dataset has been preprocessed to handle missing values and categorical data.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/joedetDS/medical-insurance-cost-prediction.git
   cd medical-insurance-prediction


#Install the required dependencies
pip install -r requirements.txt


##Usage
import joblib
model=joblib.load('regressor')
input_data_to_array=np.asarray(input_data)

input_data_reshaped=input_data_to_array.reshape(1,-1)
model.predict(input_data_reshaped)

##Model Training

In training my model i splitted the dataset into training and test datasets. I made use of 5 models and evaluated their performances
#fitting the models

#import the linear regression model
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)

#import the decision tree regressor
from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor()
dtr.fit(X_train,y_train)

#import the random forest regressor
from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor()
rfr.fit(X_train,y_train)

#import the support vector regressor
from sklearn.svm import SVR
svr=SVR()
svr.fit(X_train,y_train)

#import the Knearest neighbors regressor
from sklearn.neighbors import KNeighborsRegressor
knr=KNeighborsRegressor()
knr.fit(X_train,y_train)

pred1=lr.predict(X_test)

pred2=dtr.predict(X_test)

pred3=rfr.predict(X_test)

pred4=svr.predict(X_test)

pred5=knr.predict(X_test)


##Evaluation
I evaluated the 5 models with the R2 score metrics as well as visualizing it with a barchart to show its effectiveness. It was evident that the randomforestregressor was the best of them all.

from sklearn.metrics import r2_score

r1=round(r2_score(y_test,pred1),3)

r2=round(r2_score(y_test,pred2),3)

r3=round(r2_score(y_test,pred3),3)

r4=round(r2_score(y_test,pred4),3)

r5=round(r2_score(y_test,pred5),3)


print(f"The R-square value of logistic regression is: {r1}")

print(f"The R-square value of decision tree regressor is: {r2}")

print(f"The R-square value of random forest regressor is: {r3}")

print(f"The R-square value of support vector regressor is: {r4}")

print(f"The R-square value of k-nearest neighbors is: {r5}")

model_data={'model':['LR','DTR','RF','SVR','KNN'],
           'r_square':[r1,r2,r3,r4,r5]
           }

[Imgur](https://i.imgur.com/oUt7wcT.jpg)


##Conclusion
Feel free to reach out to @simplyedetjoseph for any questions or feedback regarding this project. Thank you for your interest in our machine learning model of medical insurance cost prediction system