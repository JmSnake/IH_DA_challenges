#---------------------------------------------
# File: DA_cha1.py
# Created: 06-May-2020
# By: Jose Manuel Garcia <jmgm.sp9@gmail.com>
#---------------------------------------------
# DATA ANALYTICS - CHALLENGE 1 - CLIENT SEGMENTATION
# 
# 1) Decide problem to solve
#       Segmentation of the clients in four groups according to id characteristics
#
# 2) Data acquisition
#       List of "customer_indices" given
#
# 3) Identifications
#       Loyal passengers -> Indices multiples of 3
#       VIP passengers -> Indices multiples of 5
#       Loyal-VIP passengers -> Indices multiples of 3 and 5
#       Regular passengers -> No match conditions above 
#	3.1) Functions 
#		Mult_3. For 3 multiplies where:  number_indice % 3 == 0 -> True (if != 0 -> False)
#		Mult_5. For 5 multiplies where:  number_indice % 5 == 0 -> True (if != 0 -> False)
#
#	3.2) Function segmentation
#		Check if indice achieve Mult_3 and Mult_5 and classification -> result segmentation (list)
# 
# 4) Count
#		Function to count the number of clients of each type. Create a dataframe (easy to check and manipulate data)
#
# 5) Plot
# 		Function to plot Horizontal Bar chart with info about clients
# 	

# Import Libraries
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager
import collections

# []DA: Data acquisition
customer_indices = [49200, 13590, 11580, 17925, 17115, 19630, 45710, 37190, 23455, 
					20815, 15515, 22505, 44260, 42545, 19565, 19149, 14253, 35412, 
					35046, 30801, 13974, 42399, 26796, 44508, 26001, 48926, 30589, 
					36997, 10271, 14866, 42599, 31388, 13492, 30328, 17564, 49499, 
					35116, 22289, 26048, 17299, 15271, 18029, 45196, 34294, 31507, 
					31429, 27506, 42271, 20894, 35707, 48484, 42479, 27148, 13732, 
					49741, 14819, 22238, 34516, 20731, 36848, 22772, 37201, 38596, 
					48121, 23497, 11198, 16762, 16711, 26399, 18466, 27043, 48679, 
					42464, 26794, 22222, 26984, 48307, 15749, 14212, 49232, 41647, 
					28618, 14606, 13687, 15533, 28306, 11042, 41302, 49978, 14254, 
					49777, 27029, 33451, 48802, 24574, 34534, 16703, 49411, 15319, 
					19961]

# Function to identify multiples of 3
def Mult_3(data):
    if data % 3 == 0:
        valid = True
    else:
        valid = False
    return valid

# Function to identify multiples of 5
def Mult_5(data):
    if data % 5 == 0:
        valid = True
    else:
        valid = False
    return valid

# 
def Segment(data):   
    segmentation = []        # empty segmentation list
    df = pd.DataFrame(columns=('Indice', 'Client type')) # empty df with indice and client type
    for i in xrange(len(data)):
        m3 = Mult_3(data[i])
        m5 = Mult_5(data[i])
        
        if m3 == True and m5 == False:
            segmentation.append('Loyal')
            df.loc[i] = [data[i], 'Loyal']
        elif m3 == False and m5 == True:
            segmentation.append('VIP')
            df.loc[i] = [data[i], 'VIP']            
        elif m3 == True and m5 == True:
            segmentation.append('Loyal-VIP')
            df.loc[i] = [data[i], 'Loyal-VIP']
        elif m3 == False and m5 == False:
            segmentation.append('Regular')
            df.loc[i] = [data[i], 'Regular']
    return segmentation, df		# complete segmentation list

# Counter how many type of client is into the list
def Counter(data):           
    counter = collections.Counter(data)
    val = counter.values()
    key = counter.keys()
    data = pd.DataFrame({'Client':key, 'Total clients': val})  #Create dataframe with info client-count
    data = data.set_index('Client')
    return data

# Data plot (Horizontal Bar Chart)
def Plt(data,type):
    data.plot(kind=type, figsize=(9, 6),color='darkblue', fontsize = 12, legend = False)
    plt.title('Number of client by type')
    plt.ylabel('Client type')
    plt.xlabel('Number of clients')    
    plt.show()

# Main
segmentation, df_clients = Segment(customer_indices)
df_count = Counter(segmentation)
Plt(df_count,'barh')

