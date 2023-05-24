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
    df = pd.read_csv("devices.csv")
    print(device_id)
    df_filtered = df.loc[df["id"] != int(device_id)]
    print(df_filtered)
    df_filtered.to_csv("devices.csv", index=False)
    
    return {"message": "yeah"}
