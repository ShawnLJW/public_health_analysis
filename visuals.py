import numpy as np
import pandas as pd
import plotly.express as px

life_expectancy = pd.read_csv('data/life-expectancy-at-birth.csv')
life_expectancy['year'] = pd.to_numeric(life_expectancy['year'])
life_expectancy['hale_years'] = pd.to_numeric(life_expectancy['hale_years'])

line_life_expectancy = px.line(life_expectancy, x='year', y='hale_years',
                               color='sex',
                               title='Life Expectancy is Increasing <br><sup>Life Expectancy at Birth</sup>')
line_life_expectancy.update_xaxes(title_text='')
line_life_expectancy.update_yaxes(title_text='')
line_life_expectancy.update_layout(legend=dict(
    title='', orientation='h', yanchor='top', y=1.1, xanchor='left', x=0))

population = pd.read_csv('data/singapore_population.csv')
population = population.melt(id_vars='Data Series')
population.columns = ['age', 'year', 'number']

population.loc[~population['age'].str.contains(
    'Years'), 'temp'] = population['age']
population['age'] = population['age'].str[2:]
population.loc[~population['age'].str.contains('Years'), 'age'] = 'All'
population['temp'] = population['temp'].fillna(method='ffill')

population.loc[population['temp'].str.contains('Male'), 'gender'] = 'Male'
population.loc[population['temp'].str.contains('Female'), 'gender'] = 'Female'
population.loc[population['temp'].str.contains(
    'Malay'), 'ethnic_group'] = 'Malay'
population.loc[population['temp'].str.contains(
    'Chinese'), 'ethnic_group'] = 'Chinese'
population.loc[population['temp'].str.contains(
    'Indian'), 'ethnic_group'] = 'Indian'
population.loc[population['temp'].str.contains(
    'Other'), 'ethnic_group'] = 'Other'
population = population.fillna('All')
population = population[['age', 'gender', 'ethnic_group', 'year', 'number']]

population['year'] = pd.to_numeric(population['year'])
population = population[population['number'] != 'na']
population['number'] = pd.to_numeric(population['number'])

elderly = pd.pivot_table(
    population[population['gender']+population['ethnic_group'] == 'AllAll'], values='number', index='year', columns='age', aggfunc='sum'
)
elderly['75 Years & Over'] = elderly['75 Years & Over'] / elderly['All']
elderly = elderly.reset_index()

line_aging_population = px.line(elderly, x='year', y='75 Years & Over',
                                title='Aging Population in Singapore <br><sup>% of Singaporeans Aged 75 and Above</sup>')
line_aging_population.update_xaxes(title_text='',
                                   range=[1980, 2021])
line_aging_population.update_yaxes(title_text='',
                                   tickformat=',.0%')

obesity_rate = pd.read_csv('data/obesity_in_primary_one.csv')
obesity_rate = obesity_rate.melt(
    var_name='year', value_name='obesity_rate').drop(0)
obesity_rate['year'] = pd.to_numeric(obesity_rate['year'])
obesity_rate['obesity_rate'] = pd.to_numeric(obesity_rate['obesity_rate'])

bar_obesity_rate = px.bar(obesity_rate, x='year', y='obesity_rate',
                          title='Obesity in Singapore <br><sup>% of Primary One Students Obese</sup>')
bar_obesity_rate.update_xaxes(title_text='',
                              tickvals=list(range(2013, 2023)))
bar_obesity_rate.update_yaxes(visible=False)

annotations = []
for i, (x, y) in obesity_rate.iterrows():
    annotations.append(
        {'x': x, 'y': y+0.5, 'text': f'{y}%', 'showarrow': False})
bar_obesity_rate.update_layout(annotations=annotations)

diagnoses_percent = pd.read_csv(
    'data/top-4-conditions-of-polyclinic-attendances.csv')
diagnoses_percent['year'] = pd.to_numeric(diagnoses_percent['year'])
diagnoses_percent['percentage_diagnoses'] = pd.to_numeric(
    diagnoses_percent['percentage_diagnoses']) / 100
diagnoses_percent['condition'] = diagnoses_percent['condition'].map({
    'Hyperlipidemia': 'High Cholestrol',
    'Hypertensive Disease': 'High Blood Pressure',
    'Acute Upper Respiratory Tract Infection including Influenza': 'Flu or Cold',
    'Diabetes Mellitus': 'Diabetes'
})

line_conditions = px.line(diagnoses_percent, x='year', y='percentage_diagnoses',
                          color='condition',
                          title='Top 4 Conditions of Polyclinic Patients')
line_conditions.update_xaxes(title_text='')
line_conditions.update_yaxes(title_text='% of Diagnoses',
                             tickvals=list(np.arange(0, 0.21, 0.05)),
                             range=[0.001, 0.2],
                             tickformat=',.0%')
line_conditions.update_layout(legend=dict(
    title='', orientation='h', yanchor='top', y=1.1, xanchor='left', x=0))

cause_of_death_percent = pd.read_csv('data/principal-causes-of-death.csv')
cause_of_death_percent['percentage_deaths'] = pd.to_numeric(
    cause_of_death_percent['percentage_deaths'])
cause_of_death_percent['rank'] = pd.to_numeric(cause_of_death_percent['rank'])
cause_of_death_percent['year'] = pd.to_numeric(cause_of_death_percent['year'])
cause_of_death_percent['disease_condition'] = cause_of_death_percent['disease_condition'].map({
    'Cancer': 'Cancer',
    'Pneumonia': 'Lung Diseases',
    'Chronic obstructive lung disease': 'Lung Diseases',
    'Chronic Obstructive Lung Disease': 'Lung Diseases',
    'Diabetes Mellitus': 'Diabetes',
    'Ischaemic heart diseases': 'Heart Diseases',
    'Ischaemic Heart Disease': 'Heart Diseases',
    'Hypertensive diseases (including hypertensive heart disease)': 'Heart Diseases',
    'Other heart diseases': 'Heart Diseases',
    'Other Heart Diseases': 'Heart Diseases',
    'Urinary tract infection': 'Urinary Tract Infection',
    'Urinary Tract Infection': 'Urinary Tract Infection',
    'Nephritis, nephrotic syndrome & nephrosis': 'Kidney Diseases',
    'Nephritis, Nephrotic Syndrome & Nephrosis': 'Kidney Diseases',
    'External causes of morbidity and mortality': 'External Causes',
    'Accidents, Poisoning & Violence': 'External Causes',
    'Cerebrovascular diseases (including stroke)': 'Cerebrovascular Diseases',
    'Cerebrovascular Disease (including stroke)': 'Cerebrovascular Diseases'
})
cause_of_death_percent = cause_of_death_percent.groupby(
    ['year', 'disease_condition'], as_index=False)['percentage_deaths'].sum()

top_death_2021 = cause_of_death_percent[cause_of_death_percent['year'] == 2021].sort_values(
    'percentage_deaths')
bar_causes_of_death = px.bar(top_death_2021,
                             x='percentage_deaths', y='disease_condition', title='Top 3 Killers in Singapore: Cancer, Heart Disease, and Lung Disease<br><sup>% of Deaths in 2021</sup>')
bar_causes_of_death.update_xaxes(visible=False)
bar_causes_of_death.update_yaxes(title_text='')

annotations = []
for x, y in zip(top_death_2021['percentage_deaths'], top_death_2021['disease_condition']):
    annotations.append({'x': x-0.5, 'y': y, 'text': f'{x:.0f}%',
                       'showarrow': False, 'font': {'color': 'white'}})
bar_causes_of_death.update_layout(annotations=annotations)
