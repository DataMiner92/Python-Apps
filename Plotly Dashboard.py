import pandas as pd
import yfinance as yf
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Initialize the Dash app
app = Dash(__name__)

# Layout of the app
app.layout = html.Div([
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date='2025-01-01',
        end_date='2025-02-01',
        display_format='YYYY-MM-DD'
    ),
    dcc.Graph(id='price-graph')
])

# Callback to update the graph based on selected dates
@app.callback(
    Output('price-graph', 'figure'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_graph(start_date, end_date):
    df = yf.download("AAP", start=start_date, end=end_date)
    
    fig = go.Figure()

    # Add close price trace
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))

    # Fill area below the close price
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], fill='tozeroy', mode='none', fillcolor='rgba(135, 206, 235, 0.2)', name='Filled Area'))

    # Update layout
    fig.update_layout(
        title='AAPL Close Price',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis=dict(tickangle=45),
        showlegend=True
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
