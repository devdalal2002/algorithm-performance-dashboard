from dash import dcc, html
import dash_bootstrap_components as dbc


def create_layout():
    return html.Div([
       
        dbc.Row([
            dbc.Col(html.H3("Algorithm Performance Dashboard", 
                           className="text-center mb-4"), width=12)
        ], className="bg-light text-dark py-2 mb-4", style={"margin-bottom": "-3%!important"}),

        
        dbc.Row([
            
            dbc.Col([
                html.Label("Number of Elements ", className="label"),
                dbc.Input(id="num-elements", type="number", 
                         placeholder="Enter number of elements you want to search from", 
                         className="input"),
                html.Button("Randomly Generate Numbers", id="generate-btn", 
                          className="button", n_clicks=0, style={"margin-top": "1.5%"}),
                html.Div(id="generated-numbers", className="output-box mt-2"),
            ], width=6, className="input-section bg-light p-3 rounded border"),

            
            dbc.Col([
                html.Label("Execution Times", className="label"),
                html.Div(id="algorithm-times", className="output-box mt-2"),
                html.Label("Target Value", className="label mt-3"),
                dbc.Input(id="target-value", type="number", 
                         placeholder="Enter target value you want to search from generated numbers", className="input"),
                html.Button("Run Algorithms", id="run-btn", 
                          className="button mt-2", n_clicks=0)
            ], width=6, className="time-section bg-light p-3 rounded border"),
        ]),

        
        dbc.Row([
            
            dbc.Col([
                html.Label("Execution Time Graph", className="label"),
                dcc.Graph(id="time-graph", config={'displayModeBar': False})
            ], width=6, className="graph-section bg-light p-3 rounded border"),

            
            dbc.Col([
                html.Label("Running Time vs Input Size Graph", className="label"),
                dcc.Graph(id="size-time-graph", config={'displayModeBar': False})
            ], width=6, className="graph-section bg-light p-3 rounded border")
        ])
    ], className="container-fluid")
