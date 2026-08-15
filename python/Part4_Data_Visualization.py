# ==========================================================
# Netflix Content Analytics
# Part 4 : Advanced Data Visualizations
# Author : Varalakshmi
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# Load Clean Dataset
# ==========================================================

df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Netflix-Content-Analytics\dataset\Netflix_Cleaned.csv")

# ==========================================================
# Chart 1 - Movies vs TV Shows (Pie Chart)
# ==========================================================

plt.figure(figsize=(6,6))
df["type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Movies vs TV Shows")
plt.ylabel("")
plt.show()

# ==========================================================
# Chart 2 - Top 10 Countries
# ==========================================================

plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Titles")
plt.xticks(rotation=45)
plt.show()

# ==========================================================
# Chart 3 - Top 10 Directors
# ==========================================================

plt.figure(figsize=(10,5))
df["director"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Titles")
plt.xticks(rotation=45)
plt.show()

# ==========================================================
# Chart 4 - Top 10 Ratings
# ==========================================================

plt.figure(figsize=(10,5))
df["rating"].value_counts().plot(kind="bar")
plt.title("Content Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Titles")
plt.xticks(rotation=45)
plt.show()

# ==========================================================
# Chart 5 - Release Year Trend
# ==========================================================

plt.figure(figsize=(10,5))
df["release_year"].value_counts().sort_index().plot()
plt.title("Content Released Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Titles")
plt.show()

# ==========================================================
# Chart 6 - Content Added by Year
# ==========================================================

plt.figure(figsize=(10,5))
df["Year_Added"].value_counts().sort_index().plot(kind="line")
plt.title("Content Added to Netflix by Year")
plt.xlabel("Year")
plt.ylabel("Titles")
plt.show()

# ==========================================================
# Chart 7 - Top Genres
# ==========================================================

plt.figure(figsize=(10,5))
df["listed_in"].value_counts().head(10).plot(kind="bar")
plt.title("Top Genres")
plt.xlabel("Genre")
plt.ylabel("Titles")
plt.xticks(rotation=45)
plt.show()

print("\nAdvanced Data Visualizations Completed Successfully!")