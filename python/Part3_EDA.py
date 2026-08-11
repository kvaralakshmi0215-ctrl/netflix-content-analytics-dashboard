# ==========================================================
# Netflix Content Analytics
# Part 3 : Exploratory Data Analysis (EDA)
# Author : Varalakshmi
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("NETFLIX CONTENT ANALYTICS")
print("PART 3 : EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ==========================================================
# Load Clean Dataset
# ==========================================================

df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Netflix-Content-Analytics\dataset\Netflix_Cleaned.csv")

# ==========================================================
# Total Records
# ==========================================================

print("\nTotal Records :", len(df))

# ==========================================================
# Movies vs TV Shows
# ==========================================================

print("\nMovies vs TV Shows")

print(df["type"].value_counts())

# ==========================================================
# Top 10 Countries
# ==========================================================

print("\nTop 10 Countries")

top_country = df["country"].value_counts().head(10)

print(top_country)

# ==========================================================
# Top 10 Directors
# ==========================================================

print("\nTop 10 Directors")

top_director = df["director"].value_counts().head(10)

print(top_director)

# ==========================================================
# Top 10 Genres
# ==========================================================

print("\nTop 10 Genres")

top_genre = df["listed_in"].value_counts().head(10)

print(top_genre)

# ==========================================================
# Rating Distribution
# ==========================================================

print("\nRatings")

print(df["rating"].value_counts())

# ==========================================================
# Release Year Distribution
# ==========================================================

print("\nRelease Year")

print(df["release_year"].value_counts().head(15))

# ==========================================================
# Content Added Every Year
# ==========================================================

print("\nContent Added by Year")

print(df["Year_Added"].value_counts().sort_index())

# ==========================================================
# Average Release Year
# ==========================================================

print("\nAverage Release Year")

print(df["release_year"].mean())

# ==========================================================
# Oldest Movie
# ==========================================================

oldest = df[df["release_year"] == df["release_year"].min()]

print("\nOldest Content")

print(oldest[["title", "release_year"]])

# ==========================================================
# Latest Movie
# ==========================================================

latest = df[df["release_year"] == df["release_year"].max()]

print("\nLatest Content")

print(latest[["title", "release_year"]])

# ==========================================================
# -------- VISUALIZATIONS ----------
# ==========================================================

# Movies vs TV Shows

plt.figure(figsize=(6,5))

df["type"].value_counts().plot(
    kind="bar"
)

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()

# ==========================================================

plt.figure(figsize=(8,5))

top_country.plot(kind="bar")

plt.title("Top 10 Countries")

plt.xlabel("Country")

plt.ylabel("Titles")

plt.show()

# ==========================================================

plt.figure(figsize=(8,5))

top_director.plot(kind="bar")

plt.title("Top 10 Directors")

plt.xlabel("Director")

plt.ylabel("Titles")

plt.xticks(rotation=45)

plt.show()

# ==========================================================

plt.figure(figsize=(8,5))

top_genre.plot(kind="bar")

plt.title("Top Genres")

plt.xlabel("Genre")

plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()

# ==========================================================

plt.figure(figsize=(8,5))

df["rating"].value_counts().plot(
    kind="bar"
)

plt.title("Content Rating Distribution")

plt.xlabel("Rating")

plt.ylabel("Titles")

plt.xticks(rotation=45)

plt.show()

# ==========================================================

plt.figure(figsize=(10,5))

df["Year_Added"].value_counts().sort_index().plot()

plt.title("Netflix Content Added Over Years")

plt.xlabel("Year")

plt.ylabel("Titles")

plt.show()

# ==========================================================

print("\nEDA COMPLETED SUCCESSFULLY")