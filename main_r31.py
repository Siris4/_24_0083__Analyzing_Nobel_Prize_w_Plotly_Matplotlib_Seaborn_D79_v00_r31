import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'birth_country_current' and count the total number of prizes won by each country
total_prizes_by_country = df.groupby('birth_country_current').size().reset_index(name='total_prizes')

# Sort by the total number of prizes won in descending order
top20_countries = total_prizes_by_country.sort_values(by='total_prizes', ascending=False).head(20)

# Set a color palette using Seaborn
colors = sns.color_palette('viridis', len(top20_countries))

# Plot a horizontal bar chart with customized colors
plt.figure(figsize=(12, 8))
plt.barh(top20_countries['birth_country_current'],
         top20_countries['total_prizes'],
         color=colors)

# Add labels and title
plt.xlabel('Total Number of Prizes Won', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.title('Top 20 Countries by Total Number of Nobel Prizes Won', fontsize=16)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest values at the top

# Adjust layout to avoid text cutoff
plt.tight_layout(pad=3.0)

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\top20_total_prizes_by_country.png"
plt.savefig(output_path)

# No need for plt.show() since we're saving the file
