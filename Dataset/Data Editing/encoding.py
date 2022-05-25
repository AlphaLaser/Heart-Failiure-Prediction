# Imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Read Data through Pandas
data = pd.read_csv("../Raw Dataset/raw_dataset.csv")

# Label encoding of Target column
le = LabelEncoder()

categorical_features = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

for i in categorical_features:
    data[i] = le.fit_transform(data[i])

# Converting Dataframe to csv file
data.to_csv("../Processed Dataset/processed_dataset.csv", index=False)

