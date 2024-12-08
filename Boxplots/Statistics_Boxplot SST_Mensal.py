import git
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Get the git root directory
git_repo = git.Repo('.', search_parent_directories=True)

#Load the SST dataset
df_sst = pd.read_csv(f"{git_repo.working_tree_dir}\\Databases\\Dataframe_sst.csv")
df_sst = df_sst.drop('Unnamed: 0', axis=1)

#Create the dataframe that will receive the data
df_stats = pd.DataFrame(columns=['Year', 'Month', 'Area', 'Mean', 'Median', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower Outliers', 'Upper Outliers'])

#For each combination area-year will be generated one boxplot
#For each of these boxplots the statistics (median, mean, min, max, quartiles and outliers) will be computed and stored in the df_stats.
for area in df_sst['state'].unique():
    for year in df_sst['year'].unique():
        df = df_sst.loc[(df_sst['state'] == area) & (df_sst['year'] == year)]
        
        #Data cleaning
        df = df.replace(-32767.0, np.nan) 

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

        #----------# Stats #----------#
        # Get the statistics of the boxplots.

        #Median 
        medians = [round(median.get_ydata()[0], 3) for median in b_plot['medians']]

        #Mean
        means = [round(mean.get_ydata()[0], 3) for mean in b_plot["means"]]

        #Min-Max
        minimums = [round(minmax.get_ydata()[0], 3) for minmax in b_plot["caps"]][::2]
        maximums = [round(minmax.get_ydata()[0], 3) for minmax in b_plot["caps"]][1::2]

        #Q1-Q3
        q1 = [round(min(q.get_ydata()), 3) for q in b_plot['boxes']]
        q3 = [round(max(q.get_ydata()), 3) for q in b_plot['boxes']]

        #Lower e Upper Outliers
        fliers = [outlier.get_ydata() for outlier in b_plot['fliers']]
        lower_outliers = []
        upper_outliers = []

        for i in range(len(fliers)):
            lower_outliers_by_box = []
            upper_outliers_by_box = []
            for outlier in fliers[i]:
                if outlier < q1[i]:
                    lower_outliers_by_box.append(round(outlier, 3))
                else:
                    upper_outliers_by_box.append(round(outlier, 3))
            lower_outliers.append(lower_outliers_by_box)
            upper_outliers.append(upper_outliers_by_box)


        stats = [medians, means, minimums, maximums, q1, q3, lower_outliers, upper_outliers]
        stats_names = ['Median', 'Mean', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower outliers', 'Upper outliers']

        categories = []
        for item in (df['month'].unique()):
            categories.append(item)


        for i in enumerate(categories):
            dict_ = {'Year': year,'Month': i[1], 'Area': area, 'Mean': means[(i[0])], 'Median': medians[(i[0])], 'Minimum': minimums[(i[0])], 'Maximum': maximums[(i[0])], 'Q1': q1[(i[0])], 'Q3': q3[(i[0])], 'Lower Outliers': lower_outliers[(i[0])], 'Upper Outliers': upper_outliers[(i[0])]}
            df_dict = pd.DataFrame([dict_])
            df_stats = pd.concat([df_stats, df_dict], ignore_index=True)

df_stats.to_csv(f'{git_repo.working_tree_dir}\\Databases\\Stats_sst.csv')