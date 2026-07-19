from collections import Counter
import plotly.express as px

from utils.map_generator import load_threats


def create_status_chart():

    threats = load_threats()

    status = [
        threat["status"]
        for threat in threats
    ]

    counts = Counter(status)

    fig = px.bar(
        x=list(counts.keys()),
        y=list(counts.values()),
        color=list(counts.keys()),
        title="Threat Status Overview"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white"),
        height=420,
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        showlegend=False
    )

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False
    )