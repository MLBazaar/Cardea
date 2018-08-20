from __future__ import absolute_import
import pandas as pd

class fhirbase(object):
    
    def set_attributes(self, dict_values):
        for attr,_ in self.__dict__.items():
            if attr in dict_values.keys():
                self.__dict__[str(attr)] = dict_values[str(attr)]

    def get_dataframe(self):
        dataframe = {}
        for attr, value in self.__dict__.items():
            if value is not None and attr != 'resourceType':
                dataframe[attr] = value

        return pd.DataFrame(dataframe)

    def assert_type(self):
        pass
    
    def check_nan(self,dict_values):
        number_of_nan =[]
        for attr, value in dict_values.items():
            summation = sum(value in ['null', nan, 'nan','NAN','Nan','NaN', 'undefined', 'unknown'] for value in value)
            percentage_of_nans = (summation/len(value))*100
            percentage_of_nans = "%.2f" % round(percentage_of_nans,2)
            number_of_nan.append({attr:[summation,percentage_of_nans]})
        return number_of_nan
    

            

    def get_relationships(self):
        return []
