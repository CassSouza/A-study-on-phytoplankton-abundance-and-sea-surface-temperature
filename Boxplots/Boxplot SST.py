import git
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Get the git root directory
git_repo = git.Repo('.', search_parent_directories=True)

#Load the SST dataset
df_sst = pd.read_csv(f"{git_repo.working_tree_dir}\\Databases\\Dataframe_sst.csv")
df_sst = df_sst.drop('Unnamed: 0', axis=1)

#Plot the Boxplot
years = [2020]
areas = ['SP']

for year in years:
    for area in df_sst['state'].unique():
        df = df_sst.loc[(df_sst['state'] == area) & (df_sst['year'] == year)]

        #Data cleaning
        df = df.replace(-32767.0, np.nan) #Ignore the Error value 

        #Styles
        medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
        meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')

        ax, b_plot = df.boxplot(column='sst', by='month', 
                            fontsize=15, grid=True, 
                            figsize=(8, 8),
                            color='black',
                            widths=0.3, 
                            meanline=False, showmeans=True, 
                            medianprops=medianprops,
                            meanprops=meanpointprops,
                            return_type='both'
                            )['sst']

        plt.ylim(10, 35)

        plt.title(f'{area} - {year}', loc='center', fontsize=18)
        plt.suptitle('')
        plt.xlabel('Month', fontsize=14)
        plt.ylabel('Temperature(C°)', fontsize=14)

        plt.savefig(f'{git_repo.working_tree_dir}\\Boxplots\\Sst plots\\Boxplot-sst {area}-{year}.jpeg', dpi=300, bbox_inches='tight')