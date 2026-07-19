import pandas as pd
import plotly.express as px

from utils.map_generator import load_threats


def create_severity_chart():

    threats = load_threats()

    df = pd.DataFrame(threats)

    severity_order = ["Critical", "High", "Medium", "Low"]

    counts = (
        df["severity"]
        .value_counts()
        .reindex(severity_order, fill_value=0)
        .reset_index()
    )

    counts.columns = ["Severity", "Count"]

    fig = px.bar(

        counts,

        x="Severity",

        y="Count",

        color="Severity",

        text="Count",

        color_discrete_map={

            "Critical": "#ff3b30",

            "High": "#ff9500",

            "Medium": "#ffd60a",

            "Low": "#34c759",

        }

    )

    fig.update_traces(textposition="outside")

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0b1220",

        plot_bgcolor="#0b1220",

        font_color="white",

        margin=dict(l=20, r=20, t=20, b=20),

        showlegend=False,

        height=320,

    )

    return fig.to_html(full_html=False)



def create_timeline_chart():

    threats = load_threats()

    df = pd.DataFrame(threats)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["Date"] = df["timestamp"].dt.date

    timeline = (

        df.groupby("Date")

        .size()

        .reset_index(name="Threats")

    )

    fig = px.line(

        timeline,

        x="Date",

        y="Threats",

        markers=True,

    )

    fig.update_traces(

        line=dict(color="#22d3ee", width=3),

        marker=dict(size=8),

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0b1220",

        plot_bgcolor="#0b1220",

        font_color="white",

        margin=dict(l=20, r=20, t=20, b=20),

        height=320,

    )

    return fig.to_html(full_html=False)