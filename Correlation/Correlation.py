import git
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

#Get the git root directory
git_repo = git.Repo('.', search_parent_directories=True)

#Load the dataset
df = pd.read_csv(f"{git_repo.working_tree_dir}\\Databases\\Dataframe_SST_chlr.csv.csv")
df = df.drop('Unnamed: 0', axis=1)

def plot_correlation(area):
    
    #There is 3 major regions in the dataset: SP, PR and SC. The forth, APA, is a sub-region of 
    # particular interest inside the SC region.

    if area == 'SP' or area == 'PR':

        df_plot = df.loc[df['Area'] == area]
        x = df_plot['Mean_temp']
        y = df_plot['Mean_chla']
        
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))

        if area == 'SP':
            ax.scatter(x,y, label=area, c='#003f5c') 
        if area == 'PR':
            ax.scatter(x,y, label=area, c='#ff6361')
        
        #Correlation fit
        statistic = stats.spearmanr(df_plot['Mean_temp'], df_plot['Mean_chla'])
        r = round(statistic[0], 2) #correlation
        p = statistic[1] #pvalue

        ax.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))
         (np.unique(x)), color='red')
    

    elif area == "SC":
        #The SC and APA will be plotted in the same plot.

        df_dual = df.loc[(df['Area'] == 'SC') | (df['Area'] == 'APA')]
        x_dual = df_dual['Mean_temp']
        y_dual = df_dual['Mean_chla']

        
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))
        
        regions = ['SC', 'APA']
        for region in regions:
            if region == 'SC':
                df_plot = df.loc[df['Area'] == region]
                x = df_plot['Mean_temp']
                y = df_plot['Mean_chla']

                ax.scatter(x,y, label=region, c='#ffa600')
            if region == 'APA':
                df_plot = df.loc[df['Area'] == region]
                x = df_plot['Mean_temp']
                y = df_plot['Mean_chla']

                ax.scatter(x,y, label=region, c='#b30000', marker='x', alpha=0.6)
        
        #Correlation fit
        statistic = stats.spearmanr(df_dual['Mean_temp'], df_dual['Mean_chla'])
        r = round(statistic[0], 2) #correlation
        p = statistic[1] #pvalue

        
        ax.plot(np.unique(x_dual), np.poly1d(np.polyfit(x_dual, y_dual, 1))
         (np.unique(x_dual)), color='red')
    
    elif area == 'all':
        x_all = df['Mean_temp']
        y_all = df['Mean_chla']

        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))

        for region in df['Area'].unique():
            df_plot = df.loc[df['Area'] == region]
            x = df_plot['Mean_temp']
            y = df_plot['Mean_chla']

            if region == 'SP':
                ax.scatter(x,y, label=region, c='#003f5c') 
            if region == 'PR':
                ax.scatter(x,y, label=region, c='#ff6361')
            if region == 'SC':
                ax.scatter(x,y, label=region, c='#ffa600')
            if region == 'APA':
                ax.scatter(x,y, label=region, c='#b30000', marker='x', alpha=0.6)
            
            #Correlation fit
            statistic = stats.spearmanr(df['Mean_temp'], df['Mean_chla'])
            r = round(statistic[0], 2) #correlation
            p = statistic[1] #pvalue

            
            ax.plot(np.unique(x_all), np.poly1d(np.polyfit(x_all, y_all, 1))
            (np.unique(x_all)), color='red')


    plt.ScalarFormatter(useMathText=True)
    plt.text(12.2,0.1, f'ρ = {r}')
    plt.text(15.8 ,0.1, f'p = {p:.2e}') 

    # Layout configs
    plt.xlim(12, 35) 
    plt.ylim(0, 6) 

    plt.title('Chl-a(mg/$m^3$) x Temperature(C°)', loc='center', fontsize=18)
    plt.xlabel('Temperature(C°)', fontsize=14)
    plt.ylabel('Chl-a(mg/$m^3$)', fontsize=14)

    plt.legend()

    plt.savefig(f'{git_repo.working_tree_dir}\\Correlation\\Correlation Examples\\{area}.jpeg', dpi=300, bbox_inches='tight')

# ------------------------------------------------------------------------------------------ #
areas = ['SP', 'PR', 'SC', 'all']
for area in areas:
    plot_correlation(area=area)