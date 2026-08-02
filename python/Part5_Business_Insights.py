# ==========================================================
# Netflix Content Analytics
# Part 5 : Business Insights
# Author : Varalakshmi
# ==========================================================

import pandas as pd

print("=" * 60)
print("NETFLIX CONTENT ANALYTICS")
print("PART 5 : BUSINESS INSIGHTS")
print("=" * 60)

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv(r"C:\Users\kanav\OneDrive\ドキュメント\Netflix-Content-Analytics\dataset\Netflix_Cleaned.csv")

# ==========================================================
# Total Titles
# ==========================================================

print("\nTotal Netflix Titles :", len(df))

# ==========================================================
# Movies vs TV Shows
# ==========================================================

print("\nMovies vs TV Shows")
print(df["type"].value_counts())

# ==========================================================
# Top Country
# ==========================================================

top_country = df["country"].value_counts().idxmax()
top_country_count = df["country"].value_counts().max()

print("\nTop Country")
print(top_country, "-", top_country_count)

# ==========================================================
# Top Director
# ==========================================================

top_director = df["director"].value_counts().idxmax()
top_director_count = df["director"].value_counts().max()

print("\nTop Director")
print(top_director, "-", top_director_count)

# ==========================================================
# Most Common Rating
# ==========================================================

top_rating = df["rating"].value_counts().idxmax()

print("\nMost Common Rating")
print(top_rating)

# ==========================================================
# Latest Release Year
# ==========================================================

print("\nLatest Release Year")
print(df["release_year"].max())

# ==========================================================
# Oldest Release Year
# ==========================================================

print("\nOldest Release Year")
print(df["release_year"].min())

# ==========================================================
# Average Release Year
# ==========================================================

print("\nAverage Release Year")
print(round(df["release_year"].mean(), 2))

# ==========================================================
# Top 5 Genres
# ==========================================================

print("\nTop 5 Genres")
print(df["listed_in"].value_counts().head())

# ==========================================================
# Top 10 Countries
# ==========================================================

print("\nTop 10 Countries")
print(df["country"].value_counts().head(10))

# ==========================================================
# Top 10 Directors
# ==========================================================

print("\nTop 10 Directors")
print(df["director"].value_counts().head(10))

# ==========================================================
# Top 10 Release Years
# ==========================================================

print("\nYears with Most Releases")
print(df["release_year"].value_counts().head(10))

# ==========================================================
# Business Summary
# ==========================================================

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS SUMMARY")
print("=" * 60)

print("1. Movies dominate the Netflix catalog.")
print("2. TV Shows represent a smaller share of the platform.")
print("3. The United States contributes the highest amount of content.")
print("4. Netflix content increased rapidly after 2015.")
print("5. TV-MA is one of the most common content ratings.")
print("6. Drama and International Movies are among the most popular genres.")
print("7. Content production has grown significantly over recent years.")
print("8. Netflix offers content from many countries, showing global reach.")

print("\nBusiness Insights Generated Successfully!")