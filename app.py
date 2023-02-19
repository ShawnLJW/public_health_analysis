from visuals import *
from dash import Dash, html, dcc

app = Dash('health_dashboard')


def index():
    layout = html.Div(children=[
        html.H1(children='How Healthy are Singaporeans?'),
        
        html.Div(children=[
            dcc.Graph(
                id='life_expectancy',
                figure=plot_life_expectancy()
            ),
            
            dcc.Graph(
                id='obesity_rate',
                figure=plot_obesity_rate()
            ),
        ], className='dual-grid'),

        dcc.Graph(
            id='aging_population',
            figure=plot_ageing_population()
        ),
        
        html.Div(children=[
            dcc.Graph(
                id='conditions',
                figure=plot_conditions()
            ),
            
            dcc.Markdown('''
                # This is an <h1> tag

                ## This is an <h2> tag

                ###### This is an <h6> tag
            ''')
        ], className='dual-grid'),
        
        html.Div(children=[
            dcc.Graph(
                id='causes_of_death',
                figure=plot_deaths()
            ),
            
            dcc.Markdown('''
                # This is an <h1> tag

                ## This is an <h2> tag

                ###### This is an <h6> tag
            ''')
        ], className='dual-grid')
    ], id='dashboard-contents')
    return layout


app.layout = index()

if __name__ == '__main__':
    app.run(debug=True)
