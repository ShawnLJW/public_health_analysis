import visuals
from dash import Dash, html, dcc

app = Dash('health_dashboard')

app.layout = html.Div(children=[
    html.H1(children='How Healthy are Singaporeans?'),

    dcc.Graph(
        id='life_expectancy',
        figure=visuals.line_life_expectancy
    ),

    dcc.Graph(
        id='aging_population',
        figure=visuals.line_aging_population
    ),

    dcc.Graph(
        id='obesity_rate',
        figure=visuals.bar_obesity_rate
    ),

    dcc.Graph(
        id='conditions',
        figure=visuals.line_conditions
    ),

    dcc.Graph(
        id='causes_of_death',
        figure=visuals.bar_causes_of_death
    )
], className='dashboard-contents')

if __name__ == '__main__':
    app.run(debug = True)