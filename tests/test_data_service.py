import unittest
import pandas as pd
from unittest.mock import patch
from services import data_service


@patch("services.data_service.pd.read_csv")
class TestDataService(unittest.TestCase):
    def test_returning_dataset_names(self, read_csv):
        test_data = {
            "Dataset_Name": ["Person Detection", "Car Detection"],
            "Location": ["data/", "data2/"],
            "Size": ["273.8 MB", "148.3"],
            "Description": ["human detection dataset", "car detection dataset"],
        }

        df = pd.DataFrame(data=test_data)

        # replace read_csv -function's return value with custom data frame
        read_csv.return_value = df
        dataset_names_mock = data_service.get_dataset_names()
        dataset_names_string = str(list(dataset_names_mock.values())[0])
        assert True == ("Person Detection" in dataset_names_string)


if __name__ == "__main__":
    unittest.main()
