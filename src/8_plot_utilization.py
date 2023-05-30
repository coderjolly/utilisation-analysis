from plotly.validators import layout
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("/Users/hsj/Desktop/utilisation-analysis/data/7_plot.csv")
days = df.Date.unique()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in days],
            value=days[0],
            clearable=False,
        ),
        dcc.Graph(id="line-chart"),
    ]
)


@app.callback(Output("line-chart", "figure"), [Input("dropdown", "value")])
def update_line_chart(day):
    mask = df["Date"] == day
    fig = px.line(
        df[mask],
        x="Time",
        y=["Simulation Utilization", "Actual Utilization"],
        range_y=[0, 100],
        range_x=[0, 23],
        title=f"System utilization for {day}",
        markers=True,
    )
    fig.update_layout(
        title="Simulation vs Actual System Utilization",
        xaxis_title="Hours",
        yaxis_title="Percentage",
        legend_title="Type",
    )
    return fig


app.run_server(debug=True)
