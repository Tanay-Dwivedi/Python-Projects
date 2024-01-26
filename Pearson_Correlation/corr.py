import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies = pd.read_csv("<your csv file>")
movies["Rotten Tomatoes"] = movies["Rotten Tomatoes"].str.replace("%", "").astype(float)
movies.drop("Type", inplace=True, axis=1)
correlations = movies.corr(method="pearson")

# Correlation Between All The Features
print(correlations)

# Correlation Between A Particular column "Year"
print(correlations["Year"])

# Visualizing Correlation

sns.heatmap(correlations)
plt.show()
