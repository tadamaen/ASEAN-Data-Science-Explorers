# Import all the necessary packages 
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns  # type: ignore
import numpy as np  # type: ignore
import plotly.express as px  # type: ignore
import plotly.graph_objects as go # type: ignore

### Data Cleaning Process
### Dataset 1 (World Life Expectancy Changes)

# Dataset 1 - World life expectancy changes dataset 
dataset1 = pd.read_csv("world_life_expectancy_changes.csv")
pd.set_option('display.max_rows', None)

# Step 1: Rename column names such that they are readable and succinct
dataset1.columns = ['Country', 'Country Code', 'Year', 'Average Life Expectancy']

# Step 2: Filter for the SEA countries (11 of them) 
dataset1_filtered = dataset1[dataset1['Country'].isin(['Brunei', 'Cambodia', 'Laos', 'Singapore', 'Myanmar', 'Malaysia', 'Philippines', 'Vietnam', 'Thailand', 'Papua New Guinea', 'Indonesia'])]

# Step 3: Remove the Country Code column as it is not needed for analysis 
dataset1_removed = dataset1_filtered[['Country', 'Year', 'Average Life Expectancy']]

# Step 4: Round the Average Life Expectancy values to 2 decimal places (instead of 4) for easy reading and visualization 
dataset1_removed.loc[:, 'Average Life Expectancy'] = dataset1_removed['Average Life Expectancy'].round(2)

# Step 5: Filter dataset by zooming in on Years 1980 to 2020 for all the SEA countries 
dataset1_filtered_years = dataset1_removed[(dataset1_removed['Year'] >= 2000) & (dataset1_removed['Year'] <= 2020)]

# Step 6: Re-Index the column numbers properly (starting from 1, representing the row numbers of the new dataset) 
dataset1_reindexed = dataset1_filtered_years.reset_index(drop = True)
dataset1_reindexed.index += 1

### Dataset 2 (Burden Of Diseases)

# Dataset 2 - Burden Of Disease dataset 
dataset2 = pd.read_csv("burden_of_disease.csv")
pd.set_option('display.max_rows', None) 

# Step 1: Rename column names such that they are readable and succinct
dataset2.columns = ['Country', 'Country Code', 'Year', 'Burden Of Disease']

# Step 2: Filter for the SEA countries (11 of them) 
dataset2_filtered = dataset2[dataset2['Country'].isin(['Brunei', 'Cambodia', 'Laos', 'Singapore', 'Myanmar', 'Malaysia', 'Philippines', 'Vietnam', 'Thailand', 'Papua New Guinea', 'Indonesia'])] 

# Step 3: Remove the Country Code column as it is not needed for analysis 
dataset2_removed = dataset2_filtered[['Country', 'Year', 'Burden Of Disease']]

# Step 4: Filter dataset by zooming in on Years 1980 to 2020 for all the SEA countries 
dataset2_filtered_years = dataset2_removed[(dataset2_removed['Year'] >= 2000) & (dataset2_removed['Year'] <= 2020)]

# Step 5: Re-Index the column numbers properly (starting from 1, representing the row numbers of the new dataset) 
dataset2_reindexed = dataset2_filtered_years.reset_index(drop = True)
dataset2_reindexed.index += 1

### Dataset 3 (Healthcare Expenditure vs GDP Dataset)

# Dataset 3 - Healthcare expenditure GDP capita dataset 
dataset3 = pd.read_csv("health_expenditure_gdp_capita.csv")
pd.set_option('display.max_rows', None) 

# Step 1: Rename column names such that they are readable and succinct
dataset3.columns = ['Country', 'Country Code', 'Year', 'Health Expenditure Per Capita', 'GDP Per Capita', 'Population', 'Continent']

# Step 2: Filter for the SEA countries (11 of them) 
dataset3_filtered = dataset3[dataset3['Country'].isin(['Brunei', 'Cambodia', 'Laos', 'Singapore', 'Myanmar', 'Malaysia', 'Philippines', 'Vietnam', 'Thailand', 'Papua New Guinea', 'Indonesia'])] 

# Step 3: Remove several columns as they are not needed for analysis 
dataset3_removed = dataset3_filtered[['Country', 'Year', 'Health Expenditure Per Capita', 'GDP Per Capita']]

# Step 4: Remove NaN rows from dataset (weird year rows like 10000BC that contain NaN figures for Health Expenditure and GDP etc.) 
dataset3_cleaned = dataset3_removed[pd.notna(dataset3_removed['Health Expenditure Per Capita']) & pd.notna(dataset3_removed['GDP Per Capita'])]

# Step 5: Round the Health Expenditure Per Capita and GDP Per Capita values to 2 decimal places (instead of 4) for easy reading and visualization 
dataset3_cleaned.loc[:, 'Health Expenditure Per Capita'] = dataset3_cleaned['Health Expenditure Per Capita'].round(2)
dataset3_cleaned.loc[:, 'GDP Per Capita'] = dataset3_cleaned['GDP Per Capita'].round(2)

# Step 6: Re-Index the column numbers properly (starting from 1, representing the row numbers of the new dataset) 
dataset3_reindexed = dataset3_cleaned.reset_index(drop = True)
dataset3_reindexed.index += 1

### Dataset 4 (Safety In Managed Sanitation)

# Dataset 4 - Safety in managed Sanitation dataset 
dataset4 = pd.read_csv("safely_managed_sanitation.csv")
dataset4

# Step 1: Rename column names such that they are readable and succinct
dataset4.columns = ['Country', 'Country Code', 'Year', 'Population Percentage With Safe Sanitation']

# Step 2: Filter for the SEA countries (11 of them) 
dataset4_filtered = dataset4[dataset4['Country'].isin(['Brunei', 'Cambodia', 'Laos', 'Singapore', 'Myanmar', 'Malaysia', 'Philippines', 'Vietnam', 'Thailand', 'Papua New Guinea', 'Indonesia'])] 

# Step 3: Remove the Country Code column as it is not needed for analysis 
dataset4_removed = dataset4_filtered[['Country', 'Year', 'Population Percentage With Safe Sanitation']]

# Step 4: Round the Population Percentage With Safe Sanitation values to 2 decimal places for easy reading and visualization 
dataset4_removed.loc[:, 'Population Percentage With Safe Sanitation'] = dataset4_removed['Population Percentage With Safe Sanitation'].round(2)

# Step 5: Filter dataset by zooming in on Years 1980 to 2020 for all the SEA countries 
dataset4_removed_filtered = dataset4_removed[(dataset4_removed['Year'] >= 2000) & (dataset4_removed['Year'] <= 2020)]

# Step 6: Re-Index the column numbers properly (starting from 1, representing the row numbers of the new dataset) 
dataset4_reindexed = dataset4_removed_filtered.reset_index(drop = True)
dataset4_reindexed.index += 1

### Dataset 1 Examination (Plot Graph And Compare With Global Average Total Life Expectancy)

# Calculating Average Life Expectancy Across The World From 2000 to 2020 (Single figures for each respective year)
dataset1_modified = dataset1[pd.notna(dataset1['Country Code'])]
dataset1_filtered_years = dataset1_modified[(dataset1_modified['Year'] >= 2000) & (dataset1_modified['Year'] <= 2020)]
average_life_expectancy_per_year = dataset1_filtered_years.groupby('Year')['Average Life Expectancy'].agg(['mean']).round(2).reset_index()
average_life_expectancy_per_year

# Plot the graph using Plotly with enhanced style (Dataset 1)
fig = px.line(dataset1_reindexed, x = 'Year', y = 'Average Life Expectancy', 
              color = 'Country', title = 'Average Life Expectancy (2000-2020) in Southeast Asian Countries',
              labels = {'Average Life Expectancy': 'Average Life Expectancy (Years)'},
              template = 'plotly_dark')

fig.update_traces(mode = 'lines+markers')

# Add a trace for the global average life expectancy
fig.add_trace(
    go.Scatter(x=average_life_expectancy_per_year['Year'], 
               y=average_life_expectancy_per_year['mean'], 
               mode='lines+markers',
               name='Global Average Life Expectancy',
               line=dict(color='white', dash='dot'))
)

fig.update_layout(
    width=1000, 
    height=600 
)

### Dataset 2 Examination (Plot Graph And Compare With Global Average Burden Of Diseases)

# Calculating Burden Of Diseases Across The World From 2000 to 2020 (Single figures for each respective year)
dataset2_modified = dataset2[pd.notna(dataset2['Country Code'])]
dataset2_filtered_years = dataset2_modified[(dataset2_modified['Year'] >= 2000) & (dataset2_modified['Year'] <= 2020)]
burden_of_diseases_per_year = dataset2_filtered_years.groupby('Year')['Burden Of Disease'].agg(['mean']).round(2).reset_index()

# Plot the graph using Plotly with enhanced style (Dataset 2)
fig = px.line(dataset2_reindexed, x = 'Year', y = 'Burden Of Disease', 
              color = 'Country', title = 'Burden Of Diseases (2000-2020) in Southeast Asian Countries',
              labels = {'Burden Of Disease': 'Burden Of Diseases (Amount)'},
              template = 'plotly_dark')

fig.update_traces(mode = 'lines+markers')

# Add a trace for the global burden of diseases
fig.add_trace(
    go.Scatter(x = burden_of_diseases_per_year['Year'], 
               y = burden_of_diseases_per_year['mean'], 
               mode = 'lines+markers',
               name = 'Global Burden Of Diseases',
               line = dict(color = 'white', dash = 'dot'))
)

fig.update_layout(
    width=1000, 
    height=600 
)

fig.show()

### Dataset 3 Examination (Plot Graph And Compare The Positions Of The SEA Countries With Reference To The Global Average Line)

# Plot the graph using Seaborn to illustrate a scatter plot of GDP Per Capita (x-axis) against Health Expenditure Per Capita (y-axis) grouped by country (hue) in 2020
# Plotly will not be appropriate in this graph due to too many variables. (Dataset 3)

# Step 7: Filter the dataset for the year 2020
dataset3_2020 = dataset3_reindexed[dataset3_reindexed['Year'] == 2020]

# Calculating and plotting the global average line in 2020 (Single figures for each respective year)
dataset3_modified = dataset3[pd.notna(dataset3['Country Code'])]
dataset3_filtered_year = dataset3_modified[(dataset3_modified['Year'] == 2020)]
dataset3_filtered_year_cleaned = dataset3_filtered_year[['Health Expenditure Per Capita', 'GDP Per Capita']]
final_dataset3 = dataset3_filtered_year_cleaned[pd.notna(dataset3_filtered_year_cleaned['Health Expenditure Per Capita']) & pd.notna(dataset3_filtered_year_cleaned['GDP Per Capita'])]
mean_health_expenditure_per_capita = final_dataset3['Health Expenditure Per Capita'].sum() / final_dataset3['Health Expenditure Per Capita'].count()
mean_gdp_per_capita = final_dataset3['GDP Per Capita'].sum() / final_dataset3['GDP Per Capita'].count()

# Calculate the slope of the line passing through the origin and the mean coordinate
slope = mean_health_expenditure_per_capita / mean_gdp_per_capita

# Calculate the x-coordinate of the top right corner of the plot area
max_gdp = dataset3_2020['GDP Per Capita'].max()

# Calculate the corresponding y-coordinate using the slope
max_health_expenditure = slope * max_gdp

# Plot the scatter plot
plt.figure(figsize = (12, 8))
scatter_plot = sns.scatterplot(data = dataset3_2020, x = 'GDP Per Capita', y = 'Health Expenditure Per Capita', hue = 'Country', palette = 'tab10', s = 100)

# Plot the line passing through the origin and the mean coordinate
plt.plot([0, max_gdp], [0, max_health_expenditure], linestyle = '--', color = 'black')
plt.annotate('Global Average Line', xy = (0.2 * max_gdp, 0.2 * max_health_expenditure), xytext = (0.15 * max_gdp, 0.45 * max_health_expenditure),
             arrowprops = dict(facecolor = 'black', arrowstyle = '->'), fontsize = 12, color = 'black')

# Extra: Customize the plot
scatter_plot.set_title('Health Expenditure vs GDP Per Capita (2020) in Southeast Asian Countries')
scatter_plot.set_xlabel('GDP Per Capita (USD)')
scatter_plot.set_ylabel('Health Expenditure Per Capita (USD)')
plt.legend(title = 'Country', bbox_to_anchor = (1.05, 1), loc = 'upper left')
plt.show()

### Dataset 4 Examination (Plot Graph And Compare With Reference To The Global Population Percentage With Safe Population) 

# Calculating Population Percentage With Safe Sanitation Across The World From 2000 to 2020 (Single figures for each respective year)
dataset4_modified = dataset4[pd.notna(dataset4['Country Code'])]
dataset4_filtered_years = dataset4_modified[(dataset4_modified['Year'] >= 2000) & (dataset4_modified['Year'] <= 2020)]
final_dataset4 = dataset4_filtered_years[pd.notna(dataset4_filtered_years['Population Percentage With Safe Sanitation'])]
population_global_safe_sanitation = final_dataset4.groupby('Year')['Population Percentage With Safe Sanitation'].agg(['mean']).round(2).reset_index()

# Plot the graph using Plotly with enhanced style (Dataset 2)
fig = px.line(dataset4_reindexed, x = 'Year', y = 'Population Percentage With Safe Sanitation', 
              color = 'Country', title = 'Population Percentage With Safe Sanitation (2000-2020) in Southeast Asian Countries',
              labels = {'Population Percentage With Safe Sanitation': 'Population Percentage With Safe Sanitation (%)'},
              template = 'plotly_dark')

fig.update_traces(mode = 'lines+markers')

fig.add_trace(
    go.Scatter(x = population_global_safe_sanitation['Year'], 
               y = population_global_safe_sanitation['mean'], 
               mode = 'lines+markers',
               name = 'Global Safe Sanitation',
               line = dict(color = 'white', dash = 'dot'))
)

fig.update_layout(
    width=1000, 
    height=600 
)

fig.show()