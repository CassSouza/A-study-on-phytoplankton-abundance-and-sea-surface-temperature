import git
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import date
from scipy import stats
import statsmodels.api as sm
from pingouin import ancova

#Get the git root directory
git_repo = git.Repo('.', search_parent_directories=True)

#Load the SST dataset
db = pd.read_csv(f"{git_repo.working_tree_dir}\\Databases\\Dataframe_sst_chlr_anual.csv")
db = db.drop('Unnamed: 0', axis=1)
db = db.query("Area != 'APA'")

#Get an array of Years
years = []
for i in db['Year'].unique():
    years.append(i)
years = np.array(years)

#Create an dataframe to store the linear regression output
df = pd.DataFrame(columns=['time','prediction', 'area'])


#Linear regression
for area in db['Area'].unique():

    #Get the data and transform to array
    df_data = db.loc[db['Area'] == area]
    data = df_data['Mean_temp'].values.reshape(-1, 1)
    data = np.concatenate(data).ravel()

    #Linear regression
    lm = LinearRegression()
    model = lm.fit(years.reshape(-1, 1), data)
    predictions = lm.predict(years.astype(float).reshape(-1, 1))

    slope, intercept, r_value, p_value, std_err = stats.linregress(data, predictions)
    tuples = list(zip(years, predictions))

    df_temporary = pd.DataFrame(tuples, columns=['time', 'prediction'])
    df_temporary['area'] = area

    df = pd.concat([df, df_temporary], ignore_index=True)

#ANCOVA Test
df['time'] = pd.to_numeric(df['time'])
ancova_stats = ancova(data=df, dv='prediction', covar='time', between='area')

ancova_values = ancova_stats.values.tolist()
f = ancova_values[0][3] #F values
p = ancova_values[0][4] #p-unc value

#Inserting the Mean_temp data
df['Mean_temp'] = db['Mean_temp']

#Plot
x_time = pd.to_datetime(years, format='%Y')

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))

for area in db['Area'].unique():
    df_plot = df.loc[df['area'] == area]

    #Get the data and transform to array
    df_data = db.loc[db['Area'] == area]
    data = df_data['Mean_temp'].values.reshape(-1, 1)
    data = np.concatenate(data).ravel()

    if area == 'SP':
        ax.scatter(x_time, data, label=area, c='#003f5c') #plotando os dados de Mean_temp
        ax.plot(x_time, df_plot['prediction'], c='#003f5c')
    
    if area == 'PR':
        ax.scatter(x_time, data, label=area, c='#ff6361') #plotando os dados de Mean_temp
        ax.plot(x_time, df_plot['prediction'], c='#ff6361')
    
    if area == 'SC':
        ax.scatter(x_time, data, label=area, c='#ffa600') #plotando os dados de Mean_temp
        ax.plot(x_time, df_plot['prediction'], c='#ffa600')

plt.title(f'ANCOVA - Temperature Variation (C°)', loc='center', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Temperature (C°)', fontsize=14)

plt.ylim(20,27) #limites eixo y
plt.xlim([pd.to_datetime('2002-06-01', format = '%Y-%m-%d'), pd.to_datetime('2023-12-01', format = '%Y-%m-%d')])

plt.legend(loc='upper right')

plt.text(pd.to_datetime('2003-02-01', format = '%Y-%m-%d'), 20.1, f'F = {f:.2e}') #F value
plt.text(pd.to_datetime('2008-02-01', format = '%Y-%m-%d'), 20.1, f'p = {p:.2e}') #p value

plt.savefig(f'{git_repo.working_tree_dir}\\Linear Regression\\Linear Regression Examples\\ANCOVA.jpeg', dpi=300, bbox_inches='tight')
