import pandas as pd

data = pd.read_csv("../Dataset/Processed Dataset/processed_dataset.csv")

# Removing the FastingBS column
del data['FastingBS']

# Remove Outliers
def remove_outliers_IQR(df):
    Q1=df.quantile(0.25)
    Q3=df.quantile(0.75)
    IQR=Q3-Q1
    df_final=df[~((df<(Q1-1.5*IQR)) | (df>(Q3+1.5*IQR)))]
    return df_final

data = remove_outliers_IQR(data)

data.to_csv("../Dataset/Final Dataset/dataset.csv", index=False)