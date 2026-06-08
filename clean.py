# importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import pymongo
from pymongo import MongoClient, errors
import glob 
import json

# initialising lists of years we iterate through 
months_years = ["01_2024", "04_2024", "07_2024", "10_2024", 
                "02_2025", "04_2025", "08_2025", "11_2025", 
                "02_2026", "05_2026"] 
years_1 = ["2021", "2022", "2023", "2024", "2025", "2026"] 
years_2 = ["2021", "2022", "2023", "2024"]

# initalising mongo connection string
client = MongoClient("mongodb+srv://<username>:<password>@ds4320proj2.p0udp7x.mongodb.net/")
database = client["DSProj2"]

### unplanned visits 
# turn city/town columns into 'city' columns 
unplanned_columns = ["Facility ID", "City", "Facility Name", 
                    "ZIP Code", "Measure ID", "Start Date", "End Date"]

unplanned_all = pd.DataFrame(unplanned_columns) 

for month_year in months_years: 
    unplanned_current = pd.read_csv(f"./hospital_data/unplanned_visits/{month_year}_unplanned_visits.csv", low_memory=False)
    if "City/Town" in list(unplanned_current.columns): 
        unplanned_current["City"] = unplanned_current["City/Town"]
    unplanned4final = unplanned_current[unplanned_columns]
    unplanned_all = pd.concat([unplanned_all, unplanned4final], ignore_index=True) 

# unplanned_all.info(verbose=True)

# prettifying spreadsheet 
unplanned_all = unplanned_all.drop([0], axis=1)
unplanned_all = unplanned_all.drop(list(range(0,8)), axis=0)
unplanned_all["ZIP"] = unplanned_all["ZIP Code"]
unplanned_all = unplanned_all.drop(["ZIP Code"], axis=1)

# converting data types 
unplanned_all["Start Date"] = pd.to_datetime(unplanned_all["Start Date"], format="%m/%d/%Y")
unplanned_all["End Date"] = pd.to_datetime(unplanned_all["End Date"], format="%m/%d/%Y") 

# double-checking our data conversion 
# unplanned_all.info()

# slide the data into mongo 
unplanned_docs = database["unplanned_data"]
unplanned_docs.insert_many(unplanned_all.to_dict("records"));

### readmission reduction data
# readmission reduction data
readm_columns = ["Facility ID", "Facility Name", "Measure Name", "Start Date", "End Date", 
                 "Excess Readmission Ratio"]

readm_all = pd.DataFrame(readm_columns) 

# read in readmin data
for month_year in months_years: 
    readm_current = pd.read_csv(f"./hospital_data/readmission_reduction/{month_year}_readm_reduc.csv")
    readm4final = readm_current[readm_columns]
    readm_all = pd.concat([readm_all, readm4final], ignore_index=True)

# readm_all.info(verbose=True)

# rename column 
readm_all["Measure ID"] = readm_all["Measure Name"] 
readm_all = readm_all.drop(["Measure Name"], axis=1)

# converting to datetime
readm_all["Start Date"] = pd.to_datetime(readm_all["Start Date"], format="%m/%d/%Y")
readm_all["End Date"] = pd.to_datetime(readm_all["End Date"], format="%m/%d/%Y")
# readm_all["End Date"].head(20)

# start date / end date EDA 
# plt.hist(readm_all["Start Date"]) 
# plt.hist(readm_all["End Date"]) 
# plt.show()

# slide the data into mongo 
readm_docs = database["readm_data"]

readm_docs.insert_many(readm_all.to_dict("records"));

### generator data 
# loop through each, slide the data into a dataframe 
generators_columns = ["Plant Name", "County", "State", "Technology"]

generators_all = pd.DataFrame(generators_columns)

for year in years_2: 
    generator_current = pd.read_csv(f"./plant_data/generator_details/eia860_generator_{year}.csv", low_memory=False)
    generator4final = generator_current[generators_columns]
    generators_all = pd.concat([generators_all, generator4final], ignore_index=True)

# generators_all.info(verbose=True)

# make prettier 
generators_all = generators_all.drop([0], axis=1)
generators_all = generators_all.drop(list(range(0,6)), axis=0)
# generators_all.head()

# slide the data into mongo 
generators_docs = database["generators_data"]

generators_docs.insert_many(generators_all.to_dict("records"));

### power plant data 
# initialise our dataframe 
plants_columns = ["Plant Name", "County", "State", "Zip"]

plants_all = pd.DataFrame(plants_columns)

for year in years_2:
    plant_current = pd.read_csv(f"./plant_data/plant_details/eia860_plant_{year}.csv")
    plant4final = plant_current[plants_columns]
    plants_all = pd.concat([plants_all, plant4final], ignore_index=True)

# plants_all.info(verbose=True)

# drop the first 6 columns. 
plants_all = plants_all.drop([0], axis=1)
plants_all = plants_all.drop(list(range(0,6)), axis=0)
plants_all["Zip"] = pd.to_numeric(plants_all["Zip"], errors="coerce")
plants_all["ZIP"] = plants_all["Zip"]
plants_all = plants_all.drop(["Zip"], axis=1)
plants_all.head()

# slide the data into mongo 
plants_docs = database["plants_data"]

plants_docs.insert_many(plants_all.to_dict("records"));

### demand data 
# initialise 
demand_columns = ["Plant Name", "Elec_MMBtu January", "Elec_MMBtu February","Elec_MMBtu March", 
                  "Elec_MMBtu April", "Elec_MMBtu May", "Elec_MMBtu June", 
                  "Elec_MMBtu July", "Elec_MMBtu August", "Elec_MMBtu September", 
                  "Elec_MMBtu October", "Elec_MMBtu November", "Elec_MMBtu December", 
                 "YEAR"]
                  
demand_all = pd.DataFrame(demand_columns)   

for year in years_1:
    demand_current = pd.read_csv(f"./demand_data/eia923_demand_{year}.csv", low_memory=False)
    # chatgpt suggested code. remove embedded newlines from column names
    # because i was struggling with why the column names couldnt be read 
    demand_current.columns = (
        demand_current.columns
        .str.replace("\n", " ", regex=False)
        .str.strip()
    )
    # my code again
    demand4final = demand_current[demand_columns]
    demand_all = pd.concat([demand_all, demand4final], ignore_index=True)


# chatgpt noticed i had a typo here. 
demand_all.info(verbose=True) 

demand_collection = database["energy_data_demand"]