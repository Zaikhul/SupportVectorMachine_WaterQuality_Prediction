# .\env_ML_WaterQuality\Scripts\activate
# deactivate

from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, precision_recall_fscore_support
from sklearn.feature_selection import SelectKBest, chi2

from libsvm.svmutil import *

import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/Data Normalization.V1.csv', delimiter=';', header=0)
data = data.dropna()
print(data.shape)
print(list(data.columns))
data.head()