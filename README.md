# Public Health Dashboard

 A Plotly Dash dashboard for analysing public health data in Singapore.

## Try it Out

### Run it Yourself

A suitable [conda](https://conda.io/) environment named `health_dashboard` can be created
and activated with:

```{shell}
conda env create -f environment.yml
conda activate health_dashboard
```

Next, run the dashbord with:

```{shell}
python app.py
```

Once app is running, visit [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your web browser.

## Data Sources

1. SingStat Table Builder
    - [Singapore Residents By Age Group, Ethnic Group And Sex, End June](https://tablebuilder.singstat.gov.sg/table/TS/M810011)
    - [Overweight And Severely Overweight (Obesity) Prevalence Among Primary One Children](https://tablebuilder.singstat.gov.sg/table/TS/M870381)

2. Data.gov.sg
    - [Top 4 Conditions of Polyclinic Attendances](https://data.gov.sg/dataset/top-4-conditions-of-polyclinic-attendances)
    - [Number of Deaths and Top 10 Principal Causes](https://data.gov.sg/dataset/principal-causes-of-death)

3. World Health Organization
    - [Life expectancy and Healthy life expectancy](https://apps.who.int/gho/data/node.main.688)
