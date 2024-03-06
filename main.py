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

