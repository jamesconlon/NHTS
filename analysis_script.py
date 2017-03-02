# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:28:56 2017

@author: James
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import NHTSdata as nhts


def getFileName(base_string, added_string = 'V2PUB',filetype = 'csv'):
    return('{0}{1}.{2}'.format(base_string,added_string,filetype))

#print(getFileName('HH'))

data_dictionary = pd.read_csv('DataDictionary.csv',nrows = 206,index_col = 'Name')


#incomes = np.array([['-9','not ascertained'],['01','< $5,000'],['02','$5,000 - $9,999'],['03','$10,000 - $14,999'],['04','$15,000 - $19,999'],['05','$20,000 - $24,999'],['06','$25,000 - $29,999'],['07','$30,000 - $34,999'],['08','$35,000 - $39,999'],['09','$40,000 - $44,999'],['10','$45,000 - $49,999'],['11','$50,000 - $54,999'],['12','$55,000 - $59,999'],['13','$60,000 - $64,999'],['14','$65,000 - $69,999'],['15','$74,000 - $79,999'],['16','$75,000 - $79,999'],['17','$80,000 - $99,999'],['18','>= $100,000']])
#incomes = np.array(['< $5,000','$5,000 - $9,999','$10,000 - $14,999','$15,000 - $19,999','$20,000 - $24,999','$25,000 - $29,999','$30,000 - $34,999','$35,000 - $39,999','$40,000 - $44,999','$45,000 - $49,999'],['$50,000 - $54,999','$55,000 - $59,999','$60,000 - $64,999','$65,000 - $69,999','$74,000 - $79,999','$75,000 - $79,999','$80,000 - $99,999','>= $100,000'])
incomes = ['< $5,000','$5,000 - $9,999','$10,000 - $14,999','$15,000 - $19,999','$20,000 - $24,999','$25,000 - $29,999','$30,000 - $34,999','$35,000 - $39,999','$40,000 - $44,999','$45,000 - $49,999','$50,000 - $54,999','$55,000 - $59,999','$60,000 - $64,999','$65,000 - $69,999','$74,000 - $79,999','$75,000 - $79,999','$80,000 - $99,999','>= $100,000']

#income_labels = incomes[:,0]
#income_ranges = incomes[:,1]
income_codes = incomes
#income_codes = pd.DataFrame(income_ranges,index = income_labels)
#print(income_codes.get_value('-9',0))

vehicle_types = ['automobile/car/station wagon','van','SUV','pickup','other truck','RV','motorcycle','golf cart']

fuel_types = ['Diesel','Natural Gas','Electricity','Gasoline']

'''
vehicle_types = np.array([['-7','Refused'],['-8','Don\'t Know'],['-9','Not ascertained'],['01', 'Automobile/car/station wagon '],['02',' Van (mini, cargo, passenger)'],['03','Sports utility vehicle'],['04',' Pickup truck'],['05','Other truck'],['06',' RV (recreational vehicle)'],['07','Motorcycle'],['08','Golf cart'],['97','Other']])
vehicle_labels = vehicle_types[:,0]
vehicle_descriptions = vehicle_types[:,1]
vehicle_codes = pd.DataFrame(vehicle_descriptions, vehicle_labels)
print(vehicle_codes.get_value('01',0))

travel_purposes = np.array([['11','Go to work'],['21','Go to school as student']])
travel_purpose_labels = travel_purposes[:,0]
travel_purpose_descriptions = travel_purposes[:,1]
travel_purpose_codes = pd.DataFrame(travel_purpose_descriptions,travel_purpose_labels)
'''

def getData(file_string, var_string):#, codes = False, code_df = ''):
    file = getFileName(file_string)
    data = pd.read_csv(file,usecols = var_string,header = 0)
    
    return(np.array(data))

def getDescription(variable):
    description = data_dictionary.get_value(variable,'Label')
    return(description)

print(getDescription('HHSIZE'))

#test_data = getData('DAY',['R_AGE'])
    
'''
HH_HHSIZE = getData('HH',['HHSIZE'])
HH_HHFAMINC = getData('HH',['HHFAMINC'])
HH_HHVEHCNT = getData('HH',['HHVEHCNT'])
'''
#PER_R_AGE = getData('PER',['R_AGE'])


'''
PER_HHFAMINC = getData('PER',['HHFAMINC'])



DAY_R_AGE = getData('DAY',['R_AGE'])
DAY_HHFAMINC = getData('DAY',['HHFAMINC'])
'''

'''
VEH_VEHTYPE = getData('VEH',['VEHTYPE'])
VEH_FUELTYPE = getData('VEH',['FUELTYPE'])
VEH_HHSIZE = getData('VEH',['HHSIZE'])
'''

#print(HHSIZE)


#age distributions







'''
data_dictionary_string = 'DataDictionary'
data_dictionary_filetype = 'csv'
data_dictionary_file = '{}.{}'.format(data_dictionary_string,data_dictionary_filetype)
data_dictionary = pd.read_csv(data_dictionary_file,nrows = 207-1)
print(len(data_dictionary))
'''
'''
household_string = 'HH'
household_filename = '{}V2PUB.csv'.format(household_string)
'''

'''
household_filename = getFileName('HH')
household_data= pd.read_csv(household_filename)

household_size_list = household_data['HHSIZE']
household_size_min = min(household_size_list)
household_size_max = max(household_size_list)
household_size_nan_count = len(household_size_list) - np.count_nonzero(~np.isnan(household_size_list))
household_size_mean = household_size_list.mean()
household_size_variance = household_size_list.var()
household_size_bins = np.arange(1,household_size_max+1)#should make sure there's no -1 values
household_size_plot_bins = household_size_bins-0.5 #this centers the bins when plotting
'''
fig = plt.gcf()
fig.set_size_inches(5,5)

#norm = stats.pdf
'''
n, bins, patches = plt.hist(household_size_list,bins = household_size_plot_bins,log = True,rwidth = .8, color = 'green', alpha = .5)
#plt.plot(bins)

log_ticks = [1,10,100,1000,10000,100000]
#plt.axis([1,14,1,100000])
#plt.yscale('log', basey = 10)
plt.yticks(log_ticks,log_ticks)
plt.xticks(household_size_bins,household_size_bins)
#plt.yticks()

plt.title('Household Size Distribution (Log Scale)')
plt.xlabel('Household Size')
plt.ylabel('Frequency')
plt.show()
'''


def makeHist(data, log = False,start = 1,offset = 0.5,title='default'):
    min_val = data.min()
    max_val = data.max()
    print(str(data))
    #data = data.apply(pd.to_numeric)#, errors='coerce')
    
    
    bins = np.arange(min_val,max_val+1)
    plot_bins = bins - offset
    
    fig = plt.gcf()
    fig.set_size_inches(8,8)
    
    n, bins, patches = plt.hist(data, bins = plot_bins, log = log, rwidth = 0.8, alpha = 0.5 )
    plt.title('Title')
    plt.xlabel('X_')
    plt.ylabel('Frequency')
    plt.show()
    
    

#makeHist(PER_R_AGE)

#(self, file_string, var_string, data_dictionary, added_string = 'V2PUB',filetype = 'csv',codes = ''):
    
'''
income_dist = nhts.NHTSdata('PER', 'HHFAMINC', data_dictionary = data_dictionary, codes = income_codes)
income_dist.plotHist(size_x = 30, size_y = 15,start = 0)
print('mean',income_dist.mean)
print('variance',income_dist.var)

a = income_dist.data

age_dist = nhts.NHTSdata('PER', 'R_AGE', data_dictionary = data_dictionary)                        #, codes = income_codes)
age_dist.plotHist(start = 5,stop = 92,size_x = 40, size_y = 15, offset = 0.0)
print('mean',age_dist.mean)
print('variance',age_dist.var)



household_size = nhts.NHTSdata('HH','HHSIZE',data_dictionary = data_dictionary)
household_size.plotHist(size_x = 30,start =1,stop = 14, size_y = 15,offset = .5)
print('mean',household_size.mean,'var',household_size.var)
'''
'''
auto_ownership = nhts.NHTSdata('HH','HHVEHCNT',data_dictionary = data_dictionary)
auto_ownership.plotHist()
print('mean',auto_ownership.mean,'variance',auto_ownership.var)
'''
'''
vehicle_type = nhts.NHTSdata('VEH','VEHTYPE',data_dictionary = data_dictionary,codes=vehicle_types)
vehicle_type.plotHist(start=1, stop = 10,offset = .5,size_x = 15, size_y = 10)
'''

'''
vehicle_fuel_type = nhts.NHTSdata('VEH','FUELTYPE',data_dictionary = data_dictionary,codes=fuel_types)
vft = vehicle_fuel_type.data
vehicle_fuel_type.plotHist(start = 1,stop =5,offset = -.5,size_x = 15, size_y = 10)

'''
'''
carpool = nhts.NHTSdata('DAY','NUMONTRP',data_dictionary = data_dictionary)
carpool.plotHist(start = 2,size_x = 15, size_y = 10)
carpool_data = carpool.data
carpool_ = carpool_data > 1
carpool_mult = carpool_*carpool_data
carpool_sum = carpool_.sum()
carpool_percent = carpool_sum / (len(carpool_data))*100
print('carpool number:',carpool_sum)
print('% carpool:',carpool_percent)
carpool_mean = carpool_mult.mean()
carpool_variance = carpool_mult.var()
print('mean',carpool_mean,'variance',carpool_variance)
'''

travel_time = nhts.NHTSdata('DAY','TRVLCMIN',data_dictionary = data_dictionary)
travel_time.plotHist(size_x = 50, size_y = 15, log = True,stop = 200)
print('travel time mean:',travel_time.mean,'travel time variance:',travel_time.var)






'''
day_data = pd.read_csv('DAYV2PUB.csv',iterator = True,chunksize= 1000)#nrows = 100)
print(day_data)

new_day_data = pd.concat(day_data,ignore_index = True)
print(new_day_data)
'''