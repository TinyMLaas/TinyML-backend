import csv
import json
 

def get_registered_devices():
    """Reads devices from a local csv file."""
    json_array = []
    
    with open("devices.csv", "r", encoding="utf-8") as csv_file:
            csvReader = csv.DictReader(csv_file)
            
            for row in csvReader:
                json_array.append(row)
    
    json_string = json.dumps(json_array)     
    
    return json_string
                                