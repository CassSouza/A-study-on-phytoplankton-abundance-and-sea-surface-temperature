#SEASONAL DECOMPOSE TEMPERATURE
import git
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Get the git root directory
git_repo = git.Repo('.', search_parent_directories=True)

#Load the SST dataset
df_sst = pd.read_csv(f"{git_repo.working_tree_dir}\\Databases\\Stats_sst.csv")
df_sst = df_sst.drop('Unnamed: 0', axis=1)

for area in df_sst['Area'].unique():
    df = df_sst.loc[df_sst['Area'] == area].copy()

    #Concat the Year and Month columns
    cols=['Year','Month']
    df['date'] = df[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")

    #Create the df for the desasonal decompose
    df_data = df[['date','Mean']].copy()
    df_data['date'] = pd.to_datetime(df_data['date'])
    df_data = df_data.set_index('date')

    #Perform the seasonal decompose
    results = sm.tsa.seasonal_decompose(df_data.asfreq('MS'), model='additive')
    observed = results.observed
    trend_estimate = results.trend
    periodic_estimate = results.seasonal
    residual = results.resid

    #Plot the seasonal decompose results
    #The plot can be made with all of the seasonal decompose components:
        #results, observed, trend_estimate, periodic_estimate, residual
    
    #Below, the plot with the trend_estimate component
    if area == 'SP':
        trend_estimate.plot(label=area, color='#003f5c', ls='-')
    elif area == 'SC':
        trend_estimate.plot(label=area, color='#ff6361', ls='-')
    elif area == 'PR':
        trend_estimate.plot(label=area, color='#ffa600', ls='-')
    elif area == 'APA':
        trend_estimate.plot(label=area, color='#b30000', ls='dotted')

    plt.title('Trend of Temperature (C°)', loc='center', fontsize=18) 
    plt.ylim(20, 28) 
    plt.legend(ncol=4) 
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)

plt.savefig(f'{git_repo.working_tree_dir}\\Seasonal Decompose\\Seasonal Decompose Examples\\trend_sst.jpeg', dpi=300, bbox_inches='tight')
