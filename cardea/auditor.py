from numpy import nan
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import json
from scipy.stats import norm

def load_checkmeta(entitysets,meta_json_filepath):
    with open(meta_json_filepath) as file:
              check_againset_meta = json.load(file)
              create_check_list(entitysets,check_againset_meta)

def create_check_list(entitysets,check_againset_meta): 
    #number of nans for all entities
    total_nans =[]
    check_list =[]
    #creating a list of all all the check fields
    for entity in entitysets.entities:
        df =  entity.df
        entity_name = entity.id
        total_nans.append(check_nan(entity_name,entity))
        fields = df.columns
        for field in fields:
            for checks in check_againset_meta[entity_name]:
                if field in checks:
                    check_list.append(checks)
    print(total_nans)                
    find_type(df,check_list)

def check_nan(entity_name,entity):
    #number of nans for a specific entity
    number_of_nan =[]
    dict_values = entity.df.to_dict('list')
    attr_value_list = []
    for attr, values in dict_values.items():
                    summation = sum(value in [nan,'null','nan','NAN','Nan','NaN', 'undefined', 'unknown'] for value in values)
                    percentage_of_nans = (summation/len(values))*100
                    percentage_of_nans = "%.2f%%" % round(percentage_of_nans,2)
                    attr_value_list.append({attr:[summation,percentage_of_nans]})
    number_of_nan.append({entity_name:attr_value_list})
    return number_of_nan


def find_type(df,check_list):
    #extract the list of checks for each column
    for checks in check_list:
    # get the column name    
        key = list(checks)[0]
    #extract all values
        attr_value = df[key].values
    #extract the list of checks for a specific column
        for check in checks[key]:
            if("distribution" in check):
                find_distribution(check["distribution"],attr_value)



def find_distribution(distributions,attr_value):
    for distribution in distributions:
        key = list(distribution)[0]
        attr = distribution[key]
        if(key == 'normal'):
            normal_distribution(attr_value, attr['min'],attr['max'],attr['mean'],attr['std'])


def normal_distribution(attr_value,min_x, max_x, mu, sigma):

    # Expected normal distribution
    x = np.linspace(min_x, max_x)
    plt.plot(x,mlab.normpdf(x, mu, sigma), linestyle='dashed')

    # Fit a normal distribution to the data:
    binwidth = 1
    bins = range(min(attr_value), max(attr_value) + binwidth, binwidth)

    mu, std = norm.fit(attr_value)

    # Plot the histogram.
    plt.hist(attr_value, bins=bins, density=True, alpha=0.6, color='g')

    # Plot the PDF.
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)
    plt.show()
