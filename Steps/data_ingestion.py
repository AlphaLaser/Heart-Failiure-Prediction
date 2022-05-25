import pandas as pd
from zenml.steps import step

class IngestData:

    def __init__(self) -> None:
        pass

    def get_data(self) -> pd.DataFrame:
        df = pd.read_csv("../Dataset/Final Dataset/dataset.csv")
        return df

@step
def ingest_data() -> pd.DataFrame:

    ingest_data = IngestData()
    df = ingest_data.get_data()
    return df
