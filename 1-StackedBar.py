import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Load GISAID data
data = pd.read_csv('/Users/aria/Downloads/gisaid_hcov-19_2025_01_13_03.tsv', sep='\t')
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
    fig.add_trace(trace, row=2, col=1)

# Update layout
fig.update_layout(title='Lineages Over Time',
                  xaxis_title='Date', yaxis_title='Count',
                  xaxis2_title='Date', yaxis2_title='%',
                  barmode='stack')
fig.show()
