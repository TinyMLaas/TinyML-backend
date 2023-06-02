import pandas as pd


# # Reads dataset names from local csv-file
# def get_dataset_names():
#     dataset = pd.read_csv("./dataset.csv")
#     dataset_names = dataset["Dataset_Name"]
#     return {"dataset_names": dataset_names}

#Returns dataset names and size
def get_dataset_names_size():
    dataset = pd.read_csv("./dataset.csv")
    dataset_names = dataset["Dataset_Name"]
    dataset_size = dataset["Size"]
    response = []
    for name,size in zip(dataset_names, dataset_size):
        response.append({"name": name, "size":size},)
    return response
