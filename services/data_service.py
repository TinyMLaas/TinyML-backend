import pandas as pd


# Reads dataset names from local csv-file
def get_dataset_names():
    dataset = pd.read_csv("./dataset.csv")
    dataset_names = dataset["Dataset_Name"]
    return {"dataset_names": dataset_names}
