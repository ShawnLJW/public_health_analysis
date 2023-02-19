import numpy as np
import pandas as pd


def get_life_expectancy():
    df = pd.read_csv('data/life_expectancy.csv')
    selected_countries = ['Singapore', 'Malaysia', 'Indonesia','Republic of Korea','Japan','Norway','United Kingdom of Great Britain and Northern Ireland', 'United States of America']
    df = df[df['country'].isin(selected_countries)]
    return df


def get_population_age():
    df = pd.read_csv('data/singapore_population.csv')
    df = df.melt(id_vars='Data Series')
    df.columns = ['age', 'year', 'number']
    df['age'] = df['age'].str[2:]

    is_not_age = ~df['age'].str.contains('Years')
    df.loc[is_not_age, 'temp'] = df['age']
    df.loc[is_not_age, 'age'] = 'All'
    df['temp'] = df['temp'].fillna(method='ffill')

    df['gender'] = df['temp'].str.extract('(Male|Female)', expand=False)
    df['ethnic_group'] = df['temp'].str.extract(
        '(Malay|Chinese|Indian|Other)', expand=False)
    df = df.fillna('All')
    df = df[['age', 'gender', 'ethnic_group', 'year', 'number']]

    df['year'] = pd.to_numeric(df['year'])
    df = df[df['number'] != 'na']
    df['number'] = pd.to_numeric(df['number'])

    df = pd.pivot_table(
        df[df['gender']+df['ethnic_group'] == 'AllAll'], values='number', index='year', columns='age', aggfunc='sum'
    )
    df['75 Years & Over'] = df['75 Years & Over'] / df['All']
    df = df.reset_index()
    df = df[['year', '75 Years & Over']]
    return df


def get_obesity_rate():
    df = pd.read_csv('data/obesity_in_primary_one.csv')
    df = df.melt(
        var_name='year', value_name='obesity_rate').drop(0)
    df['year'] = pd.to_numeric(df['year'])
    df['obesity_rate'] = pd.to_numeric(df['obesity_rate'])
    return df


def get_common_conditions():
    df = pd.read_csv(
        'data/top-4-conditions-of-polyclinic-attendances.csv')
    df['year'] = pd.to_numeric(df['year'])
    df['percentage_diagnoses'] = pd.to_numeric(
        df['percentage_diagnoses']) / 100
    df['condition'] = df['condition'].map({
        'Hyperlipidemia': 'High Cholestrol',
        'Hypertensive Disease': 'High Blood Pressure',
        'Acute Upper Respiratory Tract Infection including Influenza': 'Flu or Cold',
        'Diabetes Mellitus': 'Diabetes'
    })
    return df


def get_causes_of_death():
    df = pd.read_csv('data/principal-causes-of-death.csv')
    df['percentage_deaths'] = pd.to_numeric(
        df['percentage_deaths'])
    df['rank'] = pd.to_numeric(df['rank'])
    df['year'] = pd.to_numeric(df['year'])
    df['disease_condition'] = df['disease_condition'].map({
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
    df = df.groupby(['year', 'disease_condition'], as_index=False)
    df = df['percentage_deaths'].sum()
    df = df[df['year'] == 2021].sort_values('percentage_deaths')
    return df


life_expectancy = get_life_expectancy()
population_age = get_population_age()
obesity_rate = get_obesity_rate()
common_conditions = get_common_conditions()
causes_of_death = get_causes_of_death()
