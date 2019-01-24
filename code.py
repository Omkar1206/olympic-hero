# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)

data.head(10)
#Code starts here



# --------------
#Code starts here
data['Better_Event']=np.where((data['Total_Summer'])>=(data['Total_Winter']),'Summer','Winter')

data['Better_Event'][77]='Both'

data['Better_Event'].value_counts()
better_event='Summer'


# --------------
#Code starts here
top_countries=pd.DataFrame(data[ ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']])


top_countries.tail()

top_countries.drop(146,inplace=True)

def top_ten(top_countries,column_name):
    country_list=[]
    s=top_countries.nlargest(10,column_name)
    country_list=s['Country_Name']
    return country_list

top_10_summer=list(top_ten(top_countries=top_countries,column_name='Total_Summer'))

top_10_winter=list(top_ten(top_countries=top_countries,column_name='Total_Winter'))
top_10=list(top_ten(top_countries=top_countries,column_name='Total_Medals'))


common=['United States', 'Sweden', 'Germany', 'Soviet Union']


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]

winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

import matplotlib.pyplot as plt
import seaborn as sns


summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer')

winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter')

top_df.plot(kind='bar',x='Country_Name',y='Total_Medals')
plt.show()



# --------------
#Code starts here
summer_df['Golden_Ratio']= summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio =summer_df['Golden_Ratio'].max()

summer_country_old=summer_df[['Country_Name','Golden_Ratio']].max()
summer_country_gold='China'

winter_df['Golden_Ratio']= winter_df['Gold_Winter']/summer_df['Total_Winter']
winter_max_ratio =  winter_df['Golden_Ratio'].max()

winter_country_old= winter_df[['Country_Name','Golden_Ratio']].max()
winter_country_gold='Soviet Union'


top_df['Golden_Ratio']= top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio =         top_df['Golden_Ratio'].max()

top_country_old=        top_df[['Country_Name','Golden_Ratio']].max()
top_country_gold= 'China'


# --------------
#Code starts here
data_1=data.drop(146)
data_1['Total_Points']=(data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)


most_points=data_1['Total_Points'].max()
best_country = 'United States'


# --------------
#Code starts here
best=data[data['Country_Name']=='United States']
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


