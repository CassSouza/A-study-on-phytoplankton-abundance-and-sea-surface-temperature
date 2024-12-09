# A study on phytoplankton abundance and sea surface temperature
This repository consists of a collection of codes used in the study of the relationship between sea surface temperature (SST) and phytoplankton abundance (Chl-a), as well as future predictions and implications. 


## About the data
The data used in this study was collected and distributed free of charge by the Ocean Color portal.


## Folders

### Boxplots
The __[Boxplot folder](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/tree/main/Boxplots)__ contains the .py files necessary for creating the boxplots and also for generating the statistics related to them (e.g mean, median, quartiles...).
There is six different .py archives:

+ Chl-a related: `Use as base the 'Dataframe_chla.csv' file` (__[Dataframe_chla.csv](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/blob/main/Databases/Dataframe_chla.csv)__)

    - **Boxplot Chl-a**: Generates a boxplot of a given year (examples can be seen __[here](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/tree/main/Boxplots/Chl-a%20plots)__). 

    - **Statistics_Boxplot Chl-a_Mensal**: Computes the statistics of the data grouped by month. The result is then exported in .csv format, generating the file __[Stats_chla.csv](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/blob/main/Databases/Stats_chla.csv)__.

    - **Statistics_Boxplot Chl-a_Anual**: Computes the statistics of the data grouped by year. The result is then exported in .csv format, generating the file __[Stats_chla_Anual.csv](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/blob/main/Databases/Stats_chla_Anual.csv)__.

+ SST related: `Use as base the 'Dataframe_sst.csv' file` (__[Dataframe_sst.csv](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/blob/main/Databases/Stats_sst.csv)__)
    - **Boxplot SST**: Generates a boxplot of a given year (examples can be seen __[here](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/tree/main/Boxplots/Sst%20plots)__). 

    - **Statistics_Boxplot SST_Mensal**: Computes the statistics of the data grouped by month. The result is then exported in .csv format, generating the file __[Stats_sst.csv](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/blob/main/Databases/Stats_sst.csv)__.
     
    - **Statistics_Boxplot SST_Anual**: Computes the statistics of the data grouped by year. The result is then exported in .csv format, generating the file __[Stats_sst_Anual.csv](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/blob/main/Databases/Stats_sst_Anual.csv)__.
    

### Databases
The __[Databases folder](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/tree/main/Databases)__ contains all datasets generated for and/or by the study.

+ Initial datasets: `Data directly downloaded from the Ocean Color portal`
    - **Dataframe_chla.csv**: Chl-a data.
    - **Dataframe_sst.csv**: SST data.

+ Boxplots generated: `Data generated through the boxplots`
    - **Stats_chla.csv**: Statistics of the Chl-a data grouped by month.
    - **Stats_sst.csv**: Statistics of the SST data grouped by month.
    - **Stats_chla_Anual.csv**: Statistics of the Chl-a data grouped by year.
    - **Stats_sst_Anual.csv**: Statistics of the SST data grouped by year.


### Seasonal Decompose 
The __[Seasonal Decompose folder](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/tree/main/Seasonal%20Decompose)__ contains the .py files necessary to performe the seasonal decomposition of the data. 
All decomposition components are available, being necessary manually set what component that will be the output for the plot image.

In the example below, the output will be related to the trend component (can be seen __[here](https://github.com/CassSouza/A-study-on-phytoplankton-abundance-and-sea-surface-temperature/tree/main/Seasonal%20Decompose/Seasonal%20Decompose%20Examples)__). 

``` py
trend_estimate.plot(label=area, color='#003f5c', ls='-')
```

The others available componentes are: **observed**, **periodic_estimate** and **residual**.