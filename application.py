import numpy as np
import pandas as pd
class Application:
    def __init__(self):
        self.data=pd.DataFrame()
    def load_data(self,data):
        self.data=data
        return self.data.shape
    def describe_data(self):
        return self.data.describe()
    def clean_data(self):
        original_data=self.data.shape
        self.data.dropna(axis=0,inplace=True)
        no_of_rows_removed= original_data[0] - self.data.shape[0]
        return no_of_rows_removed