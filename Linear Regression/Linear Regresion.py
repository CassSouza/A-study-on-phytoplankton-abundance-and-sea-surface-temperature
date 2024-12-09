import git
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import date
from scipy import stats

#Get the git root directory
git_repo = git.Repo('.', search_parent_directories=True)

#Load the SST dataset
db = pd.read_csv(f"{git_repo.working_tree_dir}\\Databases\\Dataframe_sst_chlr_anual.csv")
db = db.drop('Unnamed: 0', axis=1)

for area in db['Area'].unique():
    df = db.loc[db['Area'] == area]
    df = df.reset_index()

    x=pd.to_datetime(df['Year'], format='%Y')
    y=df['Mean_temp'].values.reshape(-1, 1)

    #Linear Regression
    lm = LinearRegression()
    model = lm.fit(x.values.reshape(-1, 1),y)
    predictions = lm.predict(x.values.astype(float).reshape(-1, 1))

    y_unpacked = np.concatenate(y).ravel() 
    predictions_unpacked = np.concatenate(predictions).ravel()

    #Statistics
    slope, intercept, r_value, p_value, std_err = stats.linregress(y_unpacked, predictions_unpacked)
    r = round(slope, 3) #r squared
    p = round(p_value, 4) #p value
    b = round((predictions[1][0] - predictions[0][0]), 4) #Slope

    #Plot
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))
    ax.plot(x, predictions, c='#b30000')

    if area == 'SP':
        ax.scatter(x, y, label=area, c='#003f5c')

        plt.ylim(22,26) #limites eixo 
        plt.text(pd.to_datetime('2003-02-01', format = '%Y-%m-%d'), 22.1, f'$r^2$ = {r}') #r squared
        plt.text(pd.to_datetime('2007-02-01', format = '%Y-%m-%d'), 22.1, f'p = {p}') #p value
        plt.text(pd.to_datetime('2011-02-01', format = '%Y-%m-%d'), 22.1, f'β = {b}') #B value

    if area == 'PR':
        plt.scatter(x, y, label=area, c='#ff6361')

        plt.ylim(22,26) #limites eixo 
        plt.text(pd.to_datetime('2003-02-01', format = '%Y-%m-%d'), 22.1, f'$r^2$ = {r}') #r squared
        plt.text(pd.to_datetime('2007-02-01', format = '%Y-%m-%d'), 22.1, f'p = {p}') #p value
        plt.text(pd.to_datetime('2011-02-01', format = '%Y-%m-%d'), 22.1, f'β = {b}') #B value

    if area == 'SC':
        plt.scatter(x, y, label=area, c='#ffa600')

        plt.ylim(20,24) #limites eixo 
        plt.text(pd.to_datetime('2003-02-01', format = '%Y-%m-%d'), 20.1, f'$r^2$ = {r}') #r squared
        plt.text(pd.to_datetime('2007-02-01', format = '%Y-%m-%d'), 20.1, f'p = {p}') #p value
        plt.text(pd.to_datetime('2011-02-01', format = '%Y-%m-%d'), 20.1, f'β = {b}') #B value

    if area == 'APA':
        plt.scatter(x, y, label=area, c='#b30000', marker='x', alpha=0.6)

        plt.ylim(20,24) #limites eixo 
        plt.text(pd.to_datetime('2003-02-01', format = '%Y-%m-%d'), 20.1, f'$r^2$ = {r}') #r squared
        plt.text(pd.to_datetime('2007-02-01', format = '%Y-%m-%d'), 20.1, f'p = {p}') #p value
        plt.text(pd.to_datetime('2011-02-01', format = '%Y-%m-%d'), 20.1, f'β = {b}') #B value

    #Plot confis
    plt.title(f'Temperature Variation (C°) - {area}', loc='center', fontsize=18)
    plt.xlabel('Temperature (C°)', fontsize=14)
    plt.ylabel('Year', fontsize=14)

    plt.xlim([pd.to_datetime('2002-06-01', format = '%Y-%m-%d'), pd.to_datetime('2023-12-01', format = '%Y-%m-%d')])

    plt.legend(loc='upper right')

    plt.savefig(f'{git_repo.working_tree_dir}\\Linear Regression\\Linear Regression Examples\\LR {area}.jpeg', dpi=300, bbox_inches='tight')