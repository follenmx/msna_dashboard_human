import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd


def create_sex_distribution_pie_chart(df, column_name, fig_title):
    labels = df[column_name].value_counts().index
    values = df[column_name].value_counts().values

    # Create the pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.4,  # Donut chart style
                textinfo="label+percent+value",  # Shows label, percent, and values
                insidetextorientation="horizontal",
            )
        ]
    )

    # Update layout for a transparent background and a professional look
    fig.update_layout(
        title=fig_title,
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent background
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot area
        showlegend=True,
    )

    return fig


def create_bar_chart(dataframe, column_name, chart_title):
    # Count the occurrences of each category in the specified column
    count_series = dataframe[column_name].value_counts().sort_values(ascending=False)
    count_df = count_series.reset_index()
    count_df.columns = [column_name, "Count"]

    # Create the bar chart
    fig = px.bar(
        count_df,
        x=column_name,
        y="Count",
        title=chart_title,
        labels={"Count": "Number of Responses", column_name: "Category"},
        text="Count",
    )

    # Update the layout for a professional look
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot background
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent paper background
        font=dict(size=14),  # Font size for text
        title_font=dict(size=18),  # Font size for the title
        xaxis_title="Category",  # X-axis title
        yaxis_title="Number of Responses",  # Y-axis title
        hovermode="x",  # Hover mode
        bargap=0.2,  # Gap between bars
        height=600,  # Increase figure height
        margin=dict(b=150),  # Increase bottom margin for labels
    )
    fig.update_yaxes(range=[0, count_df["Count"].max() * 1.3])
    # Update the bar trace for a cleaner look
    fig.update_traces(
        marker_color="rgba(100, 149, 237, 0.6)",  # 'CornflowerBlue'
        marker_line_color="rgba(100, 149, 237, 1.0)",  # Bar border color
        marker_line_width=1.5,  # Bar border width
        opacity=0.9,  # Bar opacity
        textposition="outside",  # Position of the text labels
    )

    # Rotate x-axis labels to prevent overlap
    fig.update_layout(xaxis_tickangle=-45)

    return fig


def create_mbar_chart(df, column_name, option_list, bar_title):
    # Extract the relevant column
    column_data = df[column_name].dropna()

    # Initialize counts dictionary
    counts = {option: 0 for option in option_list}

    # Iterate over each response
    for response in column_data:
        for option in option_list:
            if option in response:
                counts[option] += 1

    # Convert the counts to a DataFrame
    df_counts = pd.DataFrame(list(counts.items()), columns=["Answer", "Count"])

    # Sort data for better visualization
    df_counts_sorted = df_counts.sort_values("Count", ascending=False)

    # Create the bar chart with a consistent color scheme
    fig = px.bar(
        df_counts_sorted,
        x="Answer",
        y="Count",
        text_auto=True,  # Automatically add text on bars
        title=bar_title,
        color="Answer",  # Color by answer
        color_discrete_sequence=px.colors.sequential.RdBu_r,  # Use a color scale
    )

    # Customize the chart layout
    fig.update_layout(
        xaxis_title="Options",
        yaxis_title="Count",
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="black", size=12),  # Adjust font color and size for readability
        showlegend=False,  # Hide the legend if not necessary
        height=600,  # Increase figure height
        margin=dict(b=150),  # Increase bottom margin for labels
    )

    # Rotate x-axis labels to prevent overlap
    fig.update_layout(xaxis_tickangle=-45)

    # Customize bar appearance
    fig.update_traces(
        marker_line_color="rgb(8,48,107)",  # Bar border color
        marker_line_width=1.5,  # Width of the border
        opacity=0.8,
        textangle=0,  # Set text angle to 0 for horizontal alignment
    )

    return fig


def create_histogram(df, column_name, chart_title):
    # Ensure the data is numeric and drop NaN values
    data = pd.to_numeric(df[column_name], errors="coerce").dropna()

    # Determine the number of bins using Sturges' formula
    num_bins = int(np.ceil(1 + np.log2(len(data))))

    fig = px.histogram(data, x=data, nbins=num_bins, title=chart_title, text_auto=True)
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title=column_name,
        yaxis_title="Count",
        height=500,
    )
    return fig
