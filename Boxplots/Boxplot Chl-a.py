import git
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Get the git root directory
git_repo = git.Repo('.', search_parent_directories=True)

#Load the Chl-a dataset
df_chla = pd.read_csv(f"{git_repo.working_tree_dir}\\Databases\\Dataframe_chla.csv")
df_chla = df_chla.drop('Unnamed: 0', axis=1)

#Plot the Boxplot
years = [2020]
areas = ['SP']

for year in years:
    for area in df_chla['state'].unique():
        df = df_chla.loc[(df_chla['state'] == area) & (df_chla['year'] == year)]

        #Data cleaning
        df = df.replace(-32767.0, np.nan) #Replace the error value for NaN
        df.loc[df['chlor_a'] > 8, 'chlor_a'] = np.nan 

        #Styles
        medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
        meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')

        ax, b_plot = df.boxplot(column='chlor_a', by='month', 
                            fontsize=15, grid=True, 
                            figsize=(8, 8),
                            color='black',
                            widths=0.3, 
                            meanline=False, showmeans=True, 
                            medianprops=medianprops,
                            meanprops=meanpointprops,
                            return_type='both'
                            )['chlor_a']

        plt.ylim(0, 6)

        plt.title(f'{area} - {year}', loc='center', fontsize=18)
        plt.suptitle('')
        plt.xlabel('Month', fontsize=14)
        plt.ylabel('Concentration of Chl-a (mg/$m^3$)', fontsize=14)

        plt.savefig(f'{git_repo.working_tree_dir}\\Boxplots\\Chl-a plots\\Boxplot-Chla {area}-{year}.jpeg', dpi=300, bbox_inches='tight')