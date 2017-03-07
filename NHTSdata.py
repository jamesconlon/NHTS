# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 04:36:21 2017

@author: James
"""





class NHTSdata:
    
    
    def __init__(self, file_string, var_string, data_dictionary, added_string = 'V2PUB',filetype = 'csv',codes = ''):
        import numpy as np
        import pandas as pd
       
        self.file_string = file_string
        self.var_string = []
        self.var_string.append(var_string)
       
        self.file_name = '{0}{1}.{2}'.format(self.file_string,added_string,filetype)
        self.codes = codes
        
        data = pd.read_csv(self.file_name,usecols = self.var_string,header = 0)
        self.data = np.array(data)
        
        self.data_dictionary = data_dictionary
        
        self.description = self.data_dictionary.get_value(var_string,'Label')
        
        self.mean = data.mean()
        self.var = data.var()
        
        
        
    def plotHist(self,log = False,start =0,stop = -1,offset = 0.0,title='default',size_x = 12,size_y = 12, x_log = False):
        
        import matplotlib.pyplot as plt         
        import numpy as np
        
        if title == 'default':
            title = self.description           
            
        log_string = ''
        if log == True:
            log_string = '(Log Scale)'

        if (stop == -1):
            stop = self.data.max()

        bins = np.arange(start = start,stop = stop, step = 1)
        #print('bins',bins)
        plot_bins = bins + offset


        n, new_bins, patches = plt.hist(self.data,bins = bins-offset ,log = log, rwidth = 0.8, alpha = 0.7, color = 'green' )
        
        fig = plt.gcf()
        fig.set_size_inches(size_x,size_y)


        if (len(self.codes)<=0):
            self.codes = bins
            #plot_bins = bins
            pass
            

        plt.xticks(bins,self.codes)
          
        plt.title('{0} Distribution {1}'.format(title,log_string))
        plt.xlabel(self.description)
        plt.ylabel('Frequency')
        plt.show()
        
        #return(n)
        
      
        
        
        
    def plotHistNew(self,log = False,start =0,stop = -1,offset = 0.0,title='default',size_x = 12,size_y = 12, x_log = False):  
        
        import matplotlib.pyplot as plt         
        import numpy as np        
        
        
        
        
        
        
      
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

        
        
        