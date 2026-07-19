from collections import Counter
import plotly.express as px

from utils.map_generator import load_threats


def create_country_chart():

    threats = load_threats()

    countries = [
        threat["country"]
        for threat in threats
    ]

    counts = Counter(countries)

    top = counts.most_common(10)

    x = [country for country, _ in top]
    y = [count for _, count in top]

    fig = px.bar(
        x=x,
        y=y,
        labels={
            "x": "Country",
            "y": "Threat Count"
        },
        title="Top 10 Targeted Countries"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white"),
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        height=420
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )