# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:17:26 2018

@author: muthakur
"""
#import lib
import numpy as np #math tool
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset=pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values #independent variable 
y=dataset.iloc[:,3].values   #Dependent variable

#Taking care of missing data
from sklearn.preprocessing import Imputer #Imputer is the class & imputer is object
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0) #mean of colum so axis=0
imputer=imputer.fit(x[:,1:3]) #fit in the matrix X
x[:,1:3]=imputer.transform(x[:,1:3]) #replace the missing data with mean values

#encoding categorial data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder() #LabelEncoder is the class & labelenoder_x is the obj
x[:,0]=labelencoder_x.fit_transform(x[:,0])
#Dummay Encoding
onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()
labelencoder_y=LabelEncoder() #y dependent variable so just labelencoding
y=labelencoder_y.fit_transform(y) #fit the y matrix

