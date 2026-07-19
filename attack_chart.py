from collections import Counter
import plotly.express as px

from utils.map_generator import load_threats


def create_attack_chart():

    threats = load_threats()

    attacks = [
        threat["type"]
        for threat in threats
    ]

    counts = Counter(attacks)

    labels = list(counts.keys())
    values = list(counts.values())

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.45,
        title="Attack Type Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white"),
        height=420
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )