# Imports
import pandas as pd
import seaborn as sns
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np

# Dataset
data = pd.read_csv("../Dataset/Processed Dataset/processed_dataset.csv")

# Splitting into data and target
X = data.drop('HeartDisease', axis = 1)
y = data['HeartDisease']

# Extra Trees Classifier
etc = ExtraTreesClassifier(
    n_estimators = 5,
    criterion ='entropy',
    max_features = 2
)

# Training the model
etc.fit(X, y)

# Computing the importance of each feature
feature_importance = etc.feature_importances_

# Normalizing the individual importances
feature_importance_normalized = np.std(
    [tree.feature_importances_ for tree in etc.estimators_],
    axis=0
)

# Plotting a Bar Graph to compare the models
plt.bar(X.columns, feature_importance_normalized, width = 0.7, color="orange")
plt.xlabel('Labels')
plt.ylabel('Feature Importances')
plt.title('Comparison of different Feature Importances')
plt.gcf().autofmt_xdate()
plt.show()

