import plotly.express as px
import plotly.data as pldata

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# Print first 10 lines
print("First 10 rows:")
print(df.head(10))

# Print last 10 lines
print("\nLast 10 rows:")
print(df.tail(10))

# Clean the 'strength' column: remove non-numeric chars and convert to float
df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)

# Create an interactive scatter plot: strength vs frequency, colored by direction
fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Strength vs Frequency by Direction",
                 labels={'strength': 'Strength', 'frequency': 'Frequency', 'direction': 'Direction'})

# Save plot to an HTML file
fig.write_html('wind.html')
print("Plot saved to 'wind.html'. Open it in a browser to see the interactive visualization.")
