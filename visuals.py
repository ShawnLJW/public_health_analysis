# Import processed data
from data import (
    life_expectancy,
    population_age,
    obesity_rate,
    common_conditions,
    causes_of_death
)

# Import ibraries
import numpy as np
import plotly.express as px
import plotly.io as pio
pio.templates.default = "simple_white"


def plot_life_expectancy():
    fig = px.line(life_expectancy, x='year', y='hale_years', color='sex',
                  title='Life Expectancy is Increasing <br><sup>Life Expectancy at Birth</sup>')
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='')
    fig.update_layout(legend=dict(
        title='', orientation='h', yanchor='top', y=1.1, xanchor='left', x=0))
    return fig

def plot_ageing_population():
    fig = px.line(population_age, x='year', y='75 Years & Over',
                  title='Ageing Population in Singapore <br><sup>% of Singaporeans Aged 75 and Above</sup>')
    fig.update_xaxes(title_text='', range=[1980, 2021])
    fig.update_yaxes(title_text='', tickformat=',.0%')
    return fig

def plot_obesity_rate():
    fig = px.bar(obesity_rate, x='year', y='obesity_rate',
                            title='Obesity in Singapore <br><sup>% of Primary One Students Obese</sup>')
    fig.update_xaxes(title_text='',
                                tickvals=list(range(2013, 2023)))
    fig.update_yaxes(visible=False)

    annotations = []
    for _, (x, y) in obesity_rate.iterrows():
        annotations.append(
            {'x': x, 'y': y+0.5, 'text': f'{y}%', 'showarrow': False})
    fig.update_layout(annotations=annotations)
    return fig

def plot_conditions():
    fig = px.line(common_conditions, x='year', y='percentage_diagnoses',
                  color='condition',
                  title='Top 4 Conditions of Polyclinic Patients')
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='% of Diagnoses',
                     tickvals=list(np.arange(0, 0.21, 0.05)),
                     range=[0.001, 0.2], tickformat=',.0%')
    fig.update_layout(legend=dict(
        title='', orientation='h', yanchor='top', y=1.1, xanchor='left', x=0))
    return fig

def plot_deaths():
    fig = px.bar(causes_of_death, x='percentage_deaths', y='disease_condition',
                 title='Top 3 Killers in Singapore: Cancer, Heart Disease, and Lung Disease<br><sup>% of Deaths in 2021</sup>')
    fig.update_xaxes(visible=False)
    fig.update_yaxes(title_text='')

    annotations = []
    for x, y in zip(causes_of_death['percentage_deaths'], causes_of_death['disease_condition']):
        annotations.append({'x': x-0.5, 'y': y, 'text': f'{x:.0f}%',
                        'showarrow': False, 'font': {'color': 'white'}})
    fig.update_layout(annotations=annotations)
    return fig
