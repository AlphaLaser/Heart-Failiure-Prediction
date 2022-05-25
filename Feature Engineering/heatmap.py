# Load libraries
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# load boston data
data = pd.read_csv("../Dataset/Processed Dataset/processed_dataset.csv")

# Convert to categorical data by converting data to integers
# X = X.astype(int)


# ploting the heatmap for correlation
plt.figure(figsize=(7,7))
ax = sns.heatmap(data.corr().round(2), annot=True, cmap="Oranges")
plt.show()