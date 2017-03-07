# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import NHTSdata as nhts
import matplotlib.pyplot as plt

data_dictionary = pd.read_csv('DataDictionary.csv',nrows = 206,index_col = 'Name')

n_drivers = nhts.NHTSdata('HH','DRVRCNT',data_dictionary = data_dictionary).data
n_vehicles = nhts.NHTSdata('HH','HHVEHCNT',data_dictionary = data_dictionary).data
n_workers = nhts.NHTSdata('HH','WRKCOUNT',data_dictionary = data_dictionary).data
hh_size = nhts.NHTSdata('HH','HHSIZE',data_dictionary = data_dictionary).data
urb_rur= nhts.NHTSdata('HH','URBRUR',data_dictionary = data_dictionary).data

variable_stack = np.column_stack((n_drivers,n_vehicles,n_workers,hh_size,urb_rur))

output_array = []
for i in range(len(variable_stack)):
    temp_row = variable_stack[i]
    
    drivers = temp_row[0]
    vehicles = temp_row[1]
    workers = temp_row[2]
    
    size = temp_row[3]
    size_threshold = 4
    size_above_threshold = False
    
    urban_or_rural = temp_row[4]
    is_rural = False
    
    trips_per_workday = 2
    workdays_per_week = 5
    weeks_per_year = 52
    vacation_days = 10
    holidays = 10
    carpool_percentage = 44.5/100 #number doesn't seem right
    
    work_trips_per_year = workers * trips_per_workday*(workdays_per_week*weeks_per_year - vacation_days - holidays)
    daily_work_trips = work_trips_per_year/365
    
    if (urban_or_rural == 2):
        is_rural = True
    
    if(size >= size_threshold):
        size_above_threshold = True
        
    if(size_above_threshold ==False):
        
        if(is_rural ==False):
            hh_trips = 3
        else:#is_rural == True
            hh_trips = 2
        
    else: #size_above_threshold == True
        
        if (is_rural == False):
            hh_trips = 4
        else: #is_rural == True
            hh_trips = 3
            
    daily_hh_trips = hh_trips/7
    
    max_of_drivers_and_vehicles = max(drivers,vehicles)
    daily_leisure_trips = max_of_drivers_and_vehicles * drivers
    
    total_daily_trips = daily_work_trips + daily_hh_trips + daily_leisure_trips
    
    output = np.reshape(([daily_work_trips,daily_hh_trips,daily_leisure_trips,total_daily_trips]),(1,4))
    output_array.extend(output)
    
output_array = np.reshape(output_array,(i+1,4))   

total_trips = output_array[:,3]
mean_daily_trips = np.mean(total_trips)
var_daily_trips = np.var(total_trips)
stdev_daily_trips = var_daily_trips**0.5

plot_bins = np.arange(start = 0,stop = 13, step = 1)
plot_offset_bins = plot_bins -.5
n, bins, patches = plt.hist(total_trips, bins = plot_offset_bins, rwidth = 0.8, alpha = 0.7, color = 'green' )

fig = plt.gcf()
fig.set_size_inches(12,12)

plt.xticks(plot_bins)
plt.title('Daily Household Trips')
plt.xlabel('Number of Household Trips')
plt.ylabel('Frequency')
plt.show()

print('Mean:',mean_daily_trips,'StDev:',stdev_daily_trips)