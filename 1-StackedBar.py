import matplotlib
matplotlib.use('TkAgg') 
# Now import other modules
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import argparse

def main(input_file, output_file):
    # Load GISAID data
    data = pd.read_csv(input_file, sep='\t')
    data['Collection date'] = pd.to_datetime(data['Collection date'])

    # Group by date and lineage, then count occurrences
    lineage_count = data.groupby(['Collection date', 'Lineage']).size().unstack(fill_value=0)

    # Convert the count data to long format
    lineage_count_long = lineage_count.reset_index().melt(id_vars=['Collection date'], var_name='Lineage', value_name='Count')

    # Calculate the percentage of each lineage for each date
    lineage_percentage = lineage_count.divide(lineage_count.sum(axis=1), axis=0) * 100

    # Convert the percentage data to long format
    lineage_percentage_long = lineage_percentage.reset_index().melt(id_vars=['Collection date'], var_name='Lineage', value_name='Percentage')

    # Create a subplot grid
    fig = make_subplots(rows=2, cols=1,
                        subplot_titles=('Count',
                                        'Percentage'))

    # Add the count chart
  fig_count = px.bar(lineage_count_long, x='Collection date', y='Count', color='Lineage')
    for trace in fig_count.data:
        fig.add_trace(trace, row=1, col=1)

    # Add the percentage chart
    fig_percentage = px.bar(lineage_percentage_long, x='Collection date', y='Percentage', color='Lineage')
    for trace in fig_percentage.data:
        trace.showlegend = False  # This line will hide these traces from the legend
        fig.add_trace(trace, row=2, col=1)

    # Update layout
    fig.update_layout(title='Lineages Over Time',
                      xaxis_title='Date', yaxis_title='Count',
                      xaxis2_title='Date', yaxis2_title='%',
                      barmode='stack')

    # Save the figure to HTML
    fig.write_html(output_file)

    print(f"Plot saved as HTML file at: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a Plotly bar chart from GISAID data. This script reads a TSV file containing lineage data with a 'Collection date'$
    )
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to the input TSV file. The file should contain at least two columns: "Collection date" and "Lineage".'
    )
    parser.add_argument(
        'output_file',
        type=str,
        help='Path to the output HTML file where the plot will be saved.'
    )

    args = parser.parse_args()
    main(args.input_file, args.output_file)
