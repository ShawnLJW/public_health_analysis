from visuals import *
from dash import Dash, html, dcc

app = Dash('health_dashboard')


def index():
    layout = html.Div(children=[
        html.H1(children='How Healthy are Singaporeans?'),

        dcc.Graph(
            id='life_expectancy',
            figure=plot_life_expectancy()
        ),

        dcc.Graph(
            id='aging_population',
            figure=plot_aging_population()
        ),

        dcc.Graph(
            id='obesity_rate',
            figure=plot_obesity_rate()
        ),

        dcc.Graph(
            id='conditions',
            figure=plot_conditions()
        ),

        dcc.Graph(
            id='causes_of_death',
            figure=plot_deaths()
        )
    ], className='dashboard-contents')
    return layout


app.layout = index()

if __name__ == '__main__':
    app.run(debug=True)
