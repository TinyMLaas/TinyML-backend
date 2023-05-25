import csv
import json
import pandas as pd



def get_registered_devices():
    """Reads devices from a local csv file."""
    json_array = []
    
    with open("devices.csv", "r", encoding="utf-8") as csv_file:
            csvReader = csv.DictReader(csv_file)
            
            for row in csvReader:
                json_array.append(row)
    
    json_string = json.dumps(json_array)     
    
    return json_string


def remove_device(device_id):
    device_id = int(device_id)
    
    df = pd.read_csv("devices.csv")
    
    if device_id in df["id"].values:
        df_filtered = df.loc[df["id"] != device_id]
        df_filtered.to_csv("devices.csv", index=False)
    else:
        raise ValueError()
    
    