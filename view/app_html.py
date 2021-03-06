import dash_core_components as dcc
import dash_html_components as html

import network.core.skeleton as ns
from helpers.global_constants import big_N
import helpers.global_constants as gc


def get_layout(interval_t, layouts):
    return html.Div([initial_params(interval_t), get_side_bar(layouts), get_main_body()])


def initial_params(interval_t):
    return html.Div([
        html.Link(href='/assets/codePen.css', rel='stylesheet'),
        html.Link(href='/assets/app.css', rel='stylesheet'),
        html.P(hidden='', id='raw_container', style={'display': 'none'}),
        html.P(hidden='', id='raw_container_2', style={'display': 'none'}),
        dcc.Interval(id='interval-component', interval=interval_t, n_intervals=0)
    ])


def get_main_body():
    return html.Div([
        html.Div(dcc.Graph(id='live-update-graph-network'), className="six columns"),
        html.Div(dcc.Graph(id='show-bank-status'), className="six columns"),
        html.Div(dcc.Graph(id='funnel-graph'), className="six columns"),
        html.Div(dcc.Dropdown(id='agent-bs',
                         options=[{'label': i, 'value': i} for i in gc.network_tickers],
                         value='JPM',
                         multi=False), className="two columns"),
        html.Div(dcc.Graph(id='bs-display'), className="offset nine columns")
    ], className="main")


def get_side_bar(layouts):
    return html.Div([
        html.H2("Bank Network"),
        html.Label(html.Strong('No. of Nodes', title="Number of nodes")),
        dcc.Input(id="nofbanks", value=big_N, type='number', step=1, min=1, max=big_N),
        html.Label(html.Strong('Steps')),
        dcc.Checklist(
            id='steps',
            options=[
                {'label': 'Evolve Equity', 'value': 'equity_change'},
                {'label': 'Shock!', 'value': 'apply_shock'},
                {'label': 'Deal with shock', 'value': 'deal_with_shock'}
            ],
            values=[]
        ),
        html.Label(html.Strong('Probability'), title="Probability for edge creation"),
        dcc.Input(id="prob", value=0.5, type='number', step=0.05, min=0, max=1),
        html.Label(html.Strong('M'), title='Number of edges to attach from a new node to existing nodes'),
        dcc.Input(id="m_val", value=3, type='number', step=1, min=0, max=big_N),
        html.Label(html.Strong('K-Nearest Neighbor'),
                   title='Each node is joined with its k-nearest neighbors in a ring topology.'),
        dcc.Input(id="k_val", value=4, type='number', step=1, min=0, max=big_N),
        html.Label(html.Strong('Network')),
        dcc.RadioItems(
            id='network-type-input',
            options=[{'label': i, 'value': i} for i in ns.all_nets],
            value=ns.barabasi_albert_graph
        ),
        html.Label(html.Strong('Layout')),
        dcc.RadioItems(
            id='network-layout-input',
            options=[{'label': k, 'value': k} for k in layouts],
            value="kamada_kawai_layout"
        ),
        html.Div([
            html.Label(html.Strong('Quarter', title="__ quarters ago")),
            dcc.Input(id="quarters", value=2, type='number', min=1, max=5),
            html.Button('Download BS', id='button', n_clicks=0),
            html.Div(id='data-downloader'),
            dcc.Input(style={'display': 'none'})
        ])
    ], className="side-bar")
