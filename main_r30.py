import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'birth_country_current' and 'year', and count the number of prizes won
country_year_counts = df.groupby(['birth_country_current', 'year']).size().reset_index(name='prizes_won')

# Sort by the number of prizes won in descending order
sorted_country_year_counts = country_year_counts.sort_values(by='prizes_won', ascending=False)

# Select the top 20 unique countries by their highest year
top20_countries_unique = sorted_country_year_counts.drop_duplicates(subset='birth_country_current').head(20)

# Set a color palette using Seaborn
colors = sns.color_palette('viridis', len(top20_countries_unique))

# Plot a horizontal bar chart with customized colors
plt.figure(figsize=(12, 8))
plt.barh(top20_countries_unique['birth_country_current'] + ' (' + top20_countries_unique['year'].astype(str) + ')',
         top20_countries_unique['prizes_won'],
         color=colors)

# Add labels and title
plt.xlabel('Number of Prizes Won', fontsize=14)
plt.ylabel('Country (Year)', fontsize=14)
plt.title('Top 20 Prizes Won by Unique Country and Year', fontsize=16)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest values at the top

# Adjust layout to avoid text cutoff
plt.tight_layout(pad=3.0)

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\top20_unique_prizes_won_by_country.png"
plt.savefig(output_path)

# No need for plt.show() since we're saving the file
