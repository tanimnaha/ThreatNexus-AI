import json
import plotly.express as px
import pandas as pd


def load_threats():

    with open("static/data/sample_threats.json", "r") as file:
        return json.load(file)


def create_world_map():

    threats = load_threats()

    df = pd.DataFrame(threats)

    fig = px.scatter_geo(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="country",
        hover_data={
            "city": True,
            "ip": True,
            "severity": True,
            "type": True,
            "latitude": False,
            "longitude": False,
        },
        color="severity",
        color_discrete_map={
            "Critical": "#ff3b30",
            "High": "#ff6b35",
            "Medium": "#ffd60a",
            "Low": "#22d3ee",
        },
        projection="natural earth",
        title="Global Threat Intelligence",
    )

    fig.update_geos(
        bgcolor="#07111f",
        landcolor="#132238",
        oceancolor="#07111f",
        showocean=True,
        coastlinecolor="#2d5b88",
        countrycolor="#355d8c",
    )

    fig.update_layout(
        paper_bgcolor="#07111f",
        plot_bgcolor="#07111f",
        font=dict(color="white"),
        margin=dict(l=0, r=0, t=40, b=0),
        height=420,
    )

    return fig.to_html(full_html=False)