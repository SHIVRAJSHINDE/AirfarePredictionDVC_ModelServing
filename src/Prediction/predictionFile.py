import pandas as pd  # Missing import

from src.Pipeline.s2_Data_Cleaning import DataCleaningClass
from src.Pipeline.s4_Encoding import EncodingAndScalingClass 
class Prediction_Pipeline:
    def __init__(self):
        self.data_cleaning_obj = DataCleaningClass()  # Instantiate the class
        self.Encoding_Scaling_Obj = EncodingAndScalingClass()

    def createDF(self, Airline, Date_of_Journey, Source, Destination, Dep_Time, Arrival_Time, Duration, Total_Stops):
        inputDict = {
            "Airline": [Airline],  # No need for [0] indexing
            "Date_of_Journey": [Date_of_Journey],
            "Source": [Source],
            "Destination": [Destination],
            "Route": ["Route"],
            "Dep_Time": [Dep_Time],
            "Arrival_Time": [Arrival_Time],
            "Duration": [Duration],
            "Total_Stops": [Total_Stops],
            "Additional_Info": ["Additional_Info"]
        }

        df = pd.DataFrame(inputDict)
        print("----df----")
        print(df.T)  # Transposing for display
        return df

    def reorder_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Reorders columns for the final DataFrame."""
        df = df[['Airline', 'Source', 'Destination', 'Total_Stops', 'Day', 'Month', 'Year', 
                 'Dept_Hour', 'Dept_Minute', 'Arr_Hour', 'Arr_Minute', 'hoursMinutes']]
        return df

    def receiveDataFromUI(self, Airline="Air Inida", Date_of_Journey="23-5-2024", 
                          Source="Mumbai", Destination="Bangalore", Dep_Time="22:20:00", 
                          Arrival_Time="13:15:00", Duration="2h 50m", Total_Stops="2 stops"):
    #def receiveDataFromUI(self, Airline, Date_of_Journey, Source, Destination, Dep_Time, Arrival_Time, Duration, Total_Stops):
        df = self.createDF(Airline, Date_of_Journey, Source, 
                               Destination, Dep_Time, Arrival_Time, 
                               Duration, Total_Stops)

        df = self.data_cleaning_obj.create_duration_column(df)
        df = self.data_cleaning_obj.process_date_time_columns(df)
        df = self.data_cleaning_obj.drop_unnecessary_columns(df)
        df = self.reorder_columns(df)

        print(df)

        return df
    
if __name__ == "__main__":

    Prediction_Pipeline_Obj = Prediction_Pipeline()
    Prediction_Pipeline_Obj.receiveDataFromUI()

